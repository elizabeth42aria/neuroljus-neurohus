import Link from 'next/link'

export function Footer() {
  const currentYear = new Date().getFullYear()

  const footerLinks = {
    'Verksamheter': [
      { name: 'Sök verksamheter', href: '/verksamheter' },
      { name: 'Lägg till verksamhet', href: '/verksamheter/lägg-till' },
      { name: 'Recensioner', href: '/recensioner' },
    ],
    'Community': [
      { name: 'Forum', href: '/community/forum' },
      { name: 'Privata cirklar', href: '/community/cirklar' },
      { name: 'Evenemang', href: '/community/evenemang' },
    ],
    'Academy': [
      { name: 'Kurser', href: '/academy/kurser' },
      { name: 'Certifikat', href: '/academy/certifikat' },
      { name: 'Utbildare', href: '/academy/utbildare' },
    ],
    'Resurser': [
      { name: 'Processguider', href: '/docs' },
      { name: 'Forskning', href: '/lab' },
      { name: 'Awards', href: '/awards' },
      { name: 'API', href: '/api/docs' },
    ],
    'Support': [
      { name: 'Hjälp', href: '/hjälp' },
      { name: 'Kontakt', href: '/kontakt' },
      { name: 'Integritet', href: '/integritet' },
      { name: 'Villkor', href: '/villkor' },
    ],
  }

  const socialLinks = [
    { name: 'Facebook', href: '#', icon: '📘' },
    { name: 'Twitter', href: '#', icon: '🐦' },
    { name: 'Instagram', href: '#', icon: '📷' },
    { name: 'LinkedIn', href: '#', icon: '💼' },
  ]

  return (
    <footer className="bg-neutral-900 text-white">
      <div className="container-custom">
        {/* Main footer content */}
        <div className="py-12 lg:py-16">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-8">
            {/* Brand section */}
            <div className="lg:col-span-2">
              <Link href="/" className="flex items-center space-x-2 mb-4">
                <div className="flex items-center justify-center w-10 h-10 bg-gradient-primary rounded-lg">
                  <span className="text-2xl">🧠</span>
                </div>
                <div>
                  <h3 className="text-xl font-bold">Neuroljus Neurohus</h3>
                  <p className="text-sm text-neutral-400">
                    Empati • Kunskap • Neurodiversitet
                  </p>
                </div>
              </Link>
              
              <p className="text-neutral-300 mb-6 max-w-md">
                Sveriges första digitala hus för empati, kunskap och neurodiversitet. 
                Vi skapar en plattform där familjer, assistenter, kommuner och forskare möts.
              </p>

              {/* Contact info */}
              <div className="space-y-2 text-sm text-neutral-300">
                <div className="flex items-center space-x-2">
                  <span>📧</span>
                  <span>info@neuroljus.se</span>
                </div>
                <div className="flex items-center space-x-2">
                  <span>📞</span>
                  <span>08-123 456 78</span>
                </div>
                <div className="flex items-center space-x-2">
                  <span>📍</span>
                  <span>Stockholm, Sverige</span>
                </div>
              </div>
            </div>

            {/* Links sections */}
            {Object.entries(footerLinks).map(([title, links]) => (
              <div key={title}>
                <h4 className="font-semibold text-white mb-4">{title}</h4>
                <ul className="space-y-2">
                  {links.map((link) => (
                    <li key={link.name}>
                      <Link
                        href={link.href}
                        className="text-neutral-300 hover:text-white transition-colors text-sm"
                      >
                        {link.name}
                      </Link>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>

        {/* Bottom section */}
        <div className="border-t border-neutral-800 py-6">
          <div className="flex flex-col md:flex-row items-center justify-between space-y-4 md:space-y-0">
            {/* Copyright */}
            <div className="text-sm text-neutral-400">
              © {currentYear} Neuroljus Neurohus. Alla rättigheter förbehållna.
            </div>

            {/* Social links */}
            <div className="flex items-center space-x-4">
              {socialLinks.map((social) => (
                <Link
                  key={social.name}
                  href={social.href}
                  className="text-neutral-400 hover:text-white transition-colors text-2xl"
                  aria-label={social.name}
                >
                  {social.icon}
                </Link>
              ))}
            </div>

            {/* Additional links */}
            <div className="flex items-center space-x-6 text-sm text-neutral-400">
              <Link href="/integritet" className="hover:text-white transition-colors">
                Integritet
              </Link>
              <Link href="/villkor" className="hover:text-white transition-colors">
                Villkor
              </Link>
              <Link href="/cookies" className="hover:text-white transition-colors">
                Cookies
              </Link>
            </div>
          </div>
        </div>

        {/* Mission statement */}
        <div className="border-t border-neutral-800 py-6">
          <div className="text-center">
            <div className="flex items-center justify-center space-x-2 mb-2">
              <span className="text-2xl">❤️</span>
              <span className="text-lg font-semibold">Vår mission</span>
            </div>
            <p className="text-neutral-300 max-w-3xl mx-auto">
              Neuroljus Neurohus använder AI för att stödja mänsklig empati, inte ersätta den. 
              All data hanteras med respekt för individers integritet och svensk GDPR-lagstiftning.
            </p>
          </div>
        </div>
      </div>
    </footer>
  )
}
