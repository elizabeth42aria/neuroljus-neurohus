'use client'

import { useState } from 'react'
import { Search, X } from 'lucide-react'
import { Button } from './Button'

interface SearchBarProps {
  onSearch: (query: string) => void
  placeholder?: string
  className?: string
}

export function SearchBar({ 
  onSearch, 
  placeholder = "Sök verksamheter, kurser, forskning...",
  className = ""
}: SearchBarProps) {
  const [query, setQuery] = useState('')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (query.trim()) {
      onSearch(query.trim())
    }
  }

  const handleClear = () => {
    setQuery('')
  }

  return (
    <form onSubmit={handleSubmit} className={`relative ${className}`}>
      <div className="relative">
        <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <Search className="h-4 w-4 text-neutral-400" />
        </div>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder={placeholder}
          className="block w-full pl-10 pr-10 py-2 border border-neutral-300 rounded-lg bg-white text-sm placeholder-neutral-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
        />
        {query && (
          <div className="absolute inset-y-0 right-0 pr-3 flex items-center">
            <Button
              type="button"
              variant="ghost"
              size="sm"
              onClick={handleClear}
              className="p-1 h-auto"
            >
              <X className="h-3 w-3" />
            </Button>
          </div>
        )}
      </div>
      
      <div className="mt-2 flex items-center justify-between text-xs text-neutral-500">
        <span>Tryck Enter för att söka</span>
        <div className="flex space-x-2">
          <button
            type="button"
            className="hover:text-primary-600 transition-colors"
            onClick={() => onSearch('LSS boenden')}
          >
            LSS boenden
          </button>
          <span>•</span>
          <button
            type="button"
            className="hover:text-primary-600 transition-colors"
            onClick={() => onSearch('autism kurser')}
          >
            Autism kurser
          </button>
          <span>•</span>
          <button
            type="button"
            className="hover:text-primary-600 transition-colors"
            onClick={() => onSearch('forskning')}
          >
            Forskning
          </button>
        </div>
      </div>
    </form>
  )
}
