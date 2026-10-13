import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Wingman Lab',
  description: 'Publish prototypes, send a test link, and read the signal.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
