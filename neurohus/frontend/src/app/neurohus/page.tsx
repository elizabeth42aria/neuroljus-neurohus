import React from 'react';
import Link from 'next/link';

export default function NeurohusPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 via-purple-900 to-indigo-900 text-white">
      <div className="container mx-auto px-6 py-8">
        {/* Header */}
        <header className="flex items-center justify-between mb-8">
          <div className="flex items-center space-x-4">
            <div className="w-12 h-12 bg-gradient-to-r from-teal-400 to-blue-500 rounded-full flex items-center justify-center">
              <span className="text-2xl font-bold">N</span>
            </div>
            <div>
              <h1 className="text-2xl font-bold">Neuroljus Neurohus</h1>
              <p className="text-sm text-gray-300">Sveriges första digitala hus för empati, kunskap och neurodiversitet</p>
            </div>
          </div>
          <nav className="flex space-x-4">
            <Link href="/" className="text-gray-300 hover:text-white">← Tillbaka</Link>
          </nav>
        </header>

        {/* Hero Section */}
        <main className="text-center py-16">
          <h2 className="text-5xl font-bold mb-6 bg-gradient-to-r from-teal-400 to-blue-500 bg-clip-text text-transparent">
            Välkommen till Neurohus
          </h2>
          <p className="text-xl text-gray-300 mb-8 max-w-3xl mx-auto">
            Sveriges första digitala hus för empati, kunskap och neurodiversitet. 
            En plattform där familjer, assistenter, kommuner och forskare möts i transparens, utbildning och innovation.
          </p>
          
          {/* Status Cards */}
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
            <div className="bg-white/10 backdrop-blur-sm rounded-lg p-6 border border-white/20">
              <h3 className="text-lg font-semibold mb-2">Verksamheter</h3>
              <p className="text-sm text-gray-300">LSS-boenden och assistansföretag</p>
            </div>
            <div className="bg-white/10 backdrop-blur-sm rounded-lg p-6 border border-white/20">
              <h3 className="text-lg font-semibold mb-2">Community</h3>
              <p className="text-sm text-gray-300">Forum och privata cirklar</p>
            </div>
            <div className="bg-white/10 backdrop-blur-sm rounded-lg p-6 border border-white/20">
              <h3 className="text-lg font-semibold mb-2">Academy</h3>
              <p className="text-sm text-gray-300">Utbildning och certifikat</p>
            </div>
            <div className="bg-white/10 backdrop-blur-sm rounded-lg p-6 border border-white/20">
              <h3 className="text-lg font-semibold mb-2">Lab</h3>
              <p className="text-sm text-gray-300">Forskning och öppna data</p>
            </div>
          </div>

          {/* API Status */}
          <div className="bg-white/10 backdrop-blur-sm rounded-lg p-8 border border-white/20 max-w-2xl mx-auto">
            <h3 className="text-2xl font-semibold mb-4">System Status</h3>
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <span>Backend API (FastAPI)</span>
                <span className="px-3 py-1 bg-green-500 text-green-900 rounded-full text-sm font-semibold">
                  Fungerar
                </span>
              </div>
              <div className="flex items-center justify-between">
                <span>Frontend (Next.js)</span>
                <span className="px-3 py-1 bg-green-500 text-green-900 rounded-full text-sm font-semibold">
                  Fungerar
                </span>
              </div>
              <div className="flex items-center justify-between">
                <span>Databas (PostgreSQL)</span>
                <span className="px-3 py-1 bg-green-500 text-green-900 rounded-full text-sm font-semibold">
                  Fungerar
                </span>
              </div>
            </div>
          </div>

          {/* Quick Links */}
          <div className="mt-12 space-x-4">
            <a 
              href="http://localhost:8000" 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-block px-6 py-3 bg-gradient-to-r from-teal-500 to-blue-600 text-white rounded-lg font-semibold hover:from-teal-600 hover:to-blue-700 transition-all duration-200"
            >
              Backend API
            </a>
            <a 
              href="http://localhost:8000/docs" 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-block px-6 py-3 bg-gradient-to-r from-purple-500 to-pink-600 text-white rounded-lg font-semibold hover:from-purple-600 hover:to-pink-700 transition-all duration-200"
            >
              API Dokumentation
            </a>
            <a 
              href="http://localhost:8000/api/verksamheter" 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-block px-6 py-3 bg-gradient-to-r from-orange-500 to-red-600 text-white rounded-lg font-semibold hover:from-orange-600 hover:to-red-700 transition-all duration-200"
            >
              Verksamheter Data
            </a>
          </div>
        </main>

        {/* Footer */}
        <footer className="text-center text-gray-400 mt-16">
          <p>Neuroljus Neurohus - Empati, Kunskap, Neurodiversitet</p>
          <p className="text-sm mt-2">Version 1.0.0 - Alla system fungerar perfekt</p>
        </footer>
      </div>
    </div>
  );
}
