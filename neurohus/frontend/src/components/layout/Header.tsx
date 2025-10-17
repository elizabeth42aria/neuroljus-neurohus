'use client'

import { useState } from 'react'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import { Button } from '../ui/Button'
import { SearchBar } from '../ui/SearchBar'

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const [isSearchOpen, setIsSearchOpen] = useState(false)
  const router = useRouter()

  const navigation = [
    { name: 'Hem', href: '/' },
    { name: 'Verksamheter', href: '/verksamheter' },
    { name: 'Community', href: '/community' },
    { name: 'Academy', href: '/academy' },
    { name: 'Lab', href: '/lab' },
    { name: 'Awards', href: '/awards' },
    { name: 'Guider', href: '/docs' },
  ]

  const handleSearch = (query: string) => {
    router.push(`/sök?q=${encodeURIComponent(query)}`)
    setIsSearchOpen(false)
  }

  return (
    <header className="bg-white shadow-sm border-b border-neutral-200">
      <div className="container-custom">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2">
            <div className="flex items-center justify-center w-10 h-10 bg-gradient-primary rounded-lg">
              <span className="text-2xl">🧠</span>
            </div>
            <div className="hidden sm:block">
              <h1 className="text-xl font-bold text-gradient">
                Neuroljus Neurohus
              </h1>
              <p className="text-xs text-neutral-600">
                Empati • Kunskap • Neurodiversitet
              </p>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden lg:flex items-center space-x-8">
            {navigation.map((item) => (
              <Link
                key={item.name}
                href={item.href}
                className="text-neutral-700 hover:text-primary-600 transition-colors font-medium"
              >
                {item.name}
              </Link>
            ))}
          </nav>

          {/* Right side actions */}
          <div className="flex items-center space-x-4">
            {/* Search button */}
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setIsSearchOpen(!isSearchOpen)}
              className="hidden sm:flex"
            >
              <span className="text-lg">🔍</span>
            </Button>

            {/* Language selector */}
            <Button variant="ghost" size="sm">
              <span className="text-lg">🌍</span>
              <span className="ml-1 hidden sm:inline">SV</span>
            </Button>

            {/* Mobile menu button */}
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="lg:hidden"
            >
              {isMenuOpen ? (
                <span className="text-lg">✕</span>
              ) : (
                <span className="text-lg">☰</span>
              )}
            </Button>
          </div>
        </div>

        {/* Search bar */}
        {isSearchOpen && (
          <div className="pb-4">
            <SearchBar onSearch={handleSearch} />
          </div>
        )}

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className="lg:hidden border-t border-neutral-200 py-4">
            <nav className="flex flex-col space-y-4">
              {navigation.map((item) => (
                <Link
                  key={item.name}
                  href={item.href}
                  className="text-neutral-700 hover:text-primary-600 transition-colors font-medium py-2"
                  onClick={() => setIsMenuOpen(false)}
                >
                  {item.name}
                </Link>
              ))}
              
              {/* Mobile search */}
              <div className="pt-4 border-t border-neutral-200">
                <SearchBar onSearch={handleSearch} />
              </div>
            </nav>
          </div>
        )}
      </div>
    </header>
  )
}
