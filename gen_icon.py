import os

# Create a colorful SVG icon for the kids app
svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF6B6B" />
      <stop offset="50%" stop-color="#FFA07A" />
      <stop offset="100%" stop-color="#FFD166" />
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="10" flood-opacity="0.25"/>
    </filter>
  </defs>
  <rect width="512" height="512" rx="120" fill="url(#bg)"/>
  <circle cx="256" cy="256" r="190" fill="#FFFFFF" opacity="0.9" filter="url(#shadow)"/>
  <text x="256" y="240" font-size="140" font-family="Arial, sans-serif" font-weight="900" text-anchor="middle" fill="#FF3B30">ABC</text>
  <text x="256" y="360" font-size="95" font-family="Arial, sans-serif" font-weight="900" text-anchor="middle" fill="#007AFF">1 2 3</text>
  <circle cx="120" cy="130" r="28" fill="#FFD166"/>
  <circle cx="390" cy="130" r="28" fill="#34C759"/>
  <circle cx="130" cy="380" r="24" fill="#AF52DE"/>
  <circle cx="380" cy="380" r="24" fill="#FF9500"/>
</svg>'''

with open('/var/minis/workspace/abc_kids/icon.svg', 'w') as f:
    f.write(svg_content)
print("Icon written successfully")
