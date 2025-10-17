'use client'

import { useState } from 'react'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import { 
  Heart, 
  Brain, 
  Users, 
  GraduationCap, 
  BookOpen, 
  Search,
  ArrowRight,
  Star,
  MapPin,
  Clock,
  Shield,
  Lightbulb
} from 'lucide-react'
import { Button } from '../components/ui/Button'
import { SearchBar } from '../components/ui/SearchBar'

export default function HomePage() {
  const router = useRouter()
  const [searchQuery, setSearchQuery] = useState('')

  const handleSearch = (query: string) => {
    setSearchQuery(query)
    router.push(`/sök?q=${encodeURIComponent(query)}`)
  }

  const features = [
    {
      icon: Heart,
      title: 'Empatisk AI',
      description: 'AI-teknologi som stödjer mänsklig empati och förståelse',
      color: 'text-red-500',
      bgColor: 'bg-red-50',
    },
    {
      icon: Brain,
      title: 'Neurodiversitet',
      description: 'Fokus på förståelse och respekt för olika sätt att vara',
      color: 'text-purple-500',
      bgColor: 'bg-purple-50',
    },
    {
      icon: Users,
      title: 'Community',
      description: 'Säker plats för familjer, assistenter och forskare att mötas',
      color: 'text-blue-500',
      bgColor: 'bg-blue-50',
    },
    {
      icon: GraduationCap,
      title: 'Academy',
      description: 'Utbildning och certifikat för empatisk kommunikation',
      color: 'text-green-500',
      bgColor: 'bg-green-50',
    },
  ]

  const stats = [
    { label: 'Verksamheter', value: '150+', icon: MapPin },
    { label: 'Användare', value: '2,500+', icon: Users },
    { label: 'Recensioner', value: '890+', icon: Star },
    { label: 'Kurser', value: '25+', icon: GraduationCap },
  ]

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-primary-50 to-accent-50 py-20 lg:py-32">
        <div className="container-custom">
          <div className="text-center max-w-4xl mx-auto">
            <h1 className="text-4xl lg:text-6xl font-bold text-neutral-900 mb-6">
              Välkommen till{' '}
              <span className="text-gradient">Neuroljus</span>
            </h1>
            <p className="text-xl lg:text-2xl text-neutral-600 mb-8 max-w-3xl mx-auto">
              Sveriges första digitala plattform för empati, kunskap och neurodiversitet. 
              En plattform där familjer, assistenter och forskare möts.
            </p>
            
            {/* Search Bar */}
            <div className="max-w-2xl mx-auto mb-8">
              <SearchBar onSearch={handleSearch} />
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link href="/neurohus">
                <Button size="lg" className="bg-gradient-primary">
                  Utforska Plattformen
                  <ArrowRight className="ml-2 w-4 h-4" />
                </Button>
              </Link>
              <Button size="lg" variant="outline">
                Börja kurs
                <GraduationCap className="ml-2 w-4 h-4" />
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 bg-white">
        <div className="container-custom">
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-8">
            {stats.map((stat, index) => {
              const Icon = stat.icon
              return (
                <div key={index} className="text-center">
                  <div className="flex items-center justify-center w-12 h-12 bg-primary-100 rounded-lg mx-auto mb-4">
                    <Icon className="w-6 h-6 text-primary-600" />
                  </div>
                  <div className="text-3xl font-bold text-neutral-900 mb-2">
                    {stat.value}
                  </div>
                  <div className="text-neutral-600">{stat.label}</div>
                </div>
              )
            })}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-neutral-50">
        <div className="container-custom">
          <div className="text-center mb-16">
            <h2 className="text-3xl lg:text-4xl font-bold text-neutral-900 mb-4">
              Våra funktioner
            </h2>
            <p className="text-xl text-neutral-600 max-w-3xl mx-auto">
              Vi kombinerar teknologi med empati för att skapa en bättre framtid för neurodiversitet
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => {
              const Icon = feature.icon
              return (
                <div key={index} className="card-hover">
                  <div className={`w-12 h-12 ${feature.bgColor} rounded-lg flex items-center justify-center mb-4`}>
                    <Icon className={`w-6 h-6 ${feature.color}`} />
                  </div>
                  <h3 className="text-xl font-semibold text-neutral-900 mb-2">
                    {feature.title}
                  </h3>
                  <p className="text-neutral-600">
                    {feature.description}
                  </p>
                </div>
              )
            })}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-primary">
        <div className="container-custom text-center">
          <h2 className="text-3xl lg:text-4xl font-bold text-white mb-6">
            Redo att börja din resa?
          </h2>
          <p className="text-xl text-primary-100 mb-8 max-w-2xl mx-auto">
            Gå med i vår community och upptäck hur empati och teknologi kan förändra livet för personer med neuropsykiatriska funktionsnedsättningar.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" variant="outline" className="bg-white text-primary-600 hover:bg-primary-50">
              Skapa konto
              <Users className="ml-2 w-4 h-4" />
            </Button>
            <Button size="lg" variant="ghost" className="text-white border-white hover:bg-white/10">
              Läs mer
              <BookOpen className="ml-2 w-4 h-4" />
            </Button>
          </div>
        </div>
      </section>

      {/* Trust Indicators */}
      <section className="py-16 bg-neutral-50">
        <div className="container-custom">
          <div className="text-center mb-12">
            <h2 className="text-2xl font-bold text-neutral-900 mb-4">
              Säkerhet och integritet
            </h2>
            <p className="text-neutral-600 max-w-2xl mx-auto">
              Vi tar din integritet på allvar och följer svensk GDPR-lagstiftning
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mx-auto mb-4">
                <Shield className="w-6 h-6 text-green-600" />
              </div>
              <h3 className="font-semibold text-neutral-900 mb-2">GDPR-kompatibel</h3>
              <p className="text-neutral-600 text-sm">
                All data hanteras enligt svensk GDPR-lagstiftning
              </p>
            </div>

            <div className="text-center">
              <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mx-auto mb-4">
                <Lightbulb className="w-6 h-6 text-blue-600" />
              </div>
              <h3 className="font-semibold text-neutral-900 mb-2">AI för empati</h3>
              <p className="text-neutral-600 text-sm">
                AI-teknologi som stödjer mänsklig empati, inte ersätter den
              </p>
            </div>

            <div className="text-center">
              <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mx-auto mb-4">
                <Heart className="w-6 h-6 text-purple-600" />
              </div>
              <h3 className="font-semibold text-neutral-900 mb-2">Fokus på empati</h3>
              <p className="text-neutral-600 text-sm">
                Allt vi gör är grundat i empati och förståelse för neurodiversitet
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}