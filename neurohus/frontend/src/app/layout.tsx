import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import '../styles/globals.css'
import { Header } from '../components/layout/Header'
import { Footer } from '../components/layout/Footer'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Neuroljus Neurohus',
  description: 'Sveriges första digitala hus för empati, kunskap och neurodiversitet',
  keywords: ['LSS', 'autism', 'neurodiversitet', 'empati', 'omsorg', 'assistans'],
  authors: [{ name: 'Neuroljus Neurohus' }],
  openGraph: {
    title: 'Neuroljus Neurohus',
    description: 'Sveriges första digitala hus för empati, kunskap och neurodiversitet',
    type: 'website',
    locale: 'sv_SE',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Neuroljus Neurohus',
    description: 'Sveriges första digitala hus för empati, kunskap och neurodiversitet',
  },
  robots: {
    index: true,
    follow: true,
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="sv">
      <body className={inter.className}>
        <div className="min-h-screen flex flex-col">
          <Header />
          <main className="flex-1">
            {children}
          </main>
          <Footer />
        </div>
      </body>
    </html>
  )
}
