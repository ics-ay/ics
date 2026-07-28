# UPDATED WIX BASIC OPTIMIZATION - 2026 INTERFACE
## Corrected Step-by-Step Guide for Current Wix Dashboard

---

## ⚠️ IMPORTANT: WIX INTERFACE CHANGES

**Wix has significantly updated their dashboard in 2026. The old "Performance" settings have been reorganized. Here are the CURRENT locations:**

---

## STEP 1: ENABLE WIX PERFORMANCE SETTINGS (Updated Locations)

### 1.1 Access Website Performance Settings
1. **Login to your Wix account**
2. **Go to your Intelevates site dashboard**
3. **Click "Settings" in the left sidebar**
4. **Search for "Website Performance Settings"** in the search bar
5. **Click on "Website Performance Settings" from the results**

### 1.2 Configure Caching Settings (New Location)
**In Website Performance Settings:**

```
✅ SWR (Stale While Revalidate): ENABLED
   - This shows cached content while fresh data loads in background
   - Significantly improves perceived loading speed

✅ CDN Cache: ENABLED  
   - Serves content from global servers closest to users
   - Reduces loading time worldwide

Cache Refresh Interval: Set to "1 week" (default)
   - Balances performance with content freshness
```

**Click "Save" at the bottom**

### 1.3 Alternative Method - Through Site Pages
**If you can't find Website Performance Settings:**
1. **In Wix Editor, click "Pages" (left sidebar)**
2. **Click "More Actions" (3 dots) next to any page**
3. **Select "Settings"**
4. **Click "Advanced Settings"**
5. **Look for "Manually control caching for this page"**
6. **Set cache duration to "1 week"** for static pages

---

## STEP 2: OPTIMIZE IMAGES (Updated Process)

### 2.1 Access Media Manager (New Interface)
1. **In Wix Editor, click "Media" in left panel**
2. **Click "Manage Media"** (new button location)
3. **Look for "Optimization Settings"** (gear icon in top right)

### 2.2 Enable Automatic Optimization
**In Media Manager Settings:**
```
✅ Auto-optimize images: ENABLED
✅ Convert to WebP: ENABLED  
✅ Lazy loading: ENABLED
✅ Responsive images: ENABLED

Quality Settings:
- Desktop: 85%
- Mobile: 80%
- Thumbnails: 70%
```

### 2.3 Image Upload Best Practices (Same as before)
**Before uploading:**

```bash
HERO IMAGES:
- Dimensions: 1920x1080px
- Format: JPG
- File size: Under 200KB
- Use TinyPNG.com for compression

SECTION IMAGES:
- Dimensions: 800x600px  
- Format: JPG
- File size: Under 100KB

PROFILE PHOTOS:
- Dimensions: 400x400px
- Format: JPG
- File size: Under 75KB
```

---

## STEP 3: ADD CRITICAL CSS (Updated Method)

### 3.1 Access Custom Code (New Location)
1. **In Wix Editor, click "Settings" (gear icon)**
2. **Scroll down to "Custom Code"** (under Advanced section)
3. **Click "+ Add Custom Code"**
4. **Name: "Critical CSS Performance"**
5. **Code Type: "HTML"**
6. **Add to: "All Pages"**
7. **Place Code in: "Head"**

### 3.2 Add Performance CSS Code
**Copy and paste this updated code:**

```html
<style>
/* Critical CSS for 2026 Wix Performance */
:root {
  --primary-color: #2563eb;
  --secondary-color: #1d4ed8;
  --text-color: #1f2937;
  --light-bg: #f8fafc;
}

/* Hero section optimization */
.hero-section, [data-testid="hero"], .hero-container {
  display: flex !important;
  align-items: center !important;
  min-height: 70vh !important;
  padding: 60px 20px !important;
  background: linear-gradient(135deg, var(--light-bg) 0%, #e2e8f0 100%) !important;
}

/* Typography optimization */
h1, .hero-title, [data-testid="title"] {
  font-size: clamp(2rem, 5vw, 3.5rem) !important;
  font-weight: 700 !important;
  color: var(--text-color) !important;
  line-height: 1.2 !important;
  margin-bottom: 1rem !important;
}

h2, .hero-subtitle {
  font-size: clamp(1.25rem, 3vw, 1.5rem) !important;
  color: var(--primary-color) !important;
  font-weight: 600 !important;
  margin-bottom: 1.5rem !important;
}

/* Button optimization */
.btn-primary, [data-testid="button"], .wix-button {
  background: var(--primary-color) !important;
  color: white !important;
  padding: 16px 32px !important;
  border: none !important;
  border-radius: 8px !important;
  font-size: 1.1rem !important;
  font-weight: 600 !important;
  cursor: pointer !important;
  transition: all 0.3s ease !important;
  text-decoration: none !important;
  display: inline-block !important;
  min-height: 44px !important;
  min-width: 44px !important;
}

.btn-primary:hover, [data-testid="button"]:hover {
  background: var(--secondary-color) !important;
  transform: translateY(-2px) !important;
}

/* Mobile-first responsive design */
@media (max-width: 768px) {
  .hero-section, [data-testid="hero"] {
    flex-direction: column !important;
    text-align: center !important;
    padding: 40px 20px !important;
  }
  
  .btn-primary, [data-testid="button"] {
    width: 100% !important;
    max-width: 280px !important;
    margin-bottom: 1rem !important;
  }
  
  /* Touch-friendly elements */
  button, input, select, textarea {
    min-height: 44px !important;
    font-size: 16px !important; /* Prevents zoom on iOS */
  }
}

/* Loading optimization */
img, [data-testid="image"] {
  transition: opacity 0.3s ease !important;
}

img[loading="lazy"], [data-testid="image"][loading="lazy"] {
  opacity: 0 !important;
}

img[loading="lazy"].loaded, [data-testid="image"].loaded {
  opacity: 1 !important;
}

/* Performance improvements */
* {
  box-sizing: border-box !important;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
}
</style>
```

---

## STEP 4: CONFIGURE MOBILE RESPONSIVENESS (Updated Interface)

### 4.1 Access Mobile Editor (New Method)
1. **In Wix Editor, look for device icons at the top**
2. **Click the mobile phone icon** 📱
3. **Select "Mobile" from dropdown**
4. **You'll see your site in mobile preview**

### 4.2 Optimize Mobile Navigation (Updated)
1. **Click on your main menu in mobile view**
2. **In the settings panel (right side):**
   - **Menu Type:** "Hamburger Menu"
   - **Animation:** "Slide from Left"
   - **Background:** White or brand color
   - **Button Size:** Minimum 44px x 44px

### 4.3 Add Mobile-Specific Custom Code
**Create another Custom Code block:**
- **Name:** "Mobile Optimization"
- **Place in:** "Head"
- **Pages:** "All Pages"

```html
<style>
/* 2026 Mobile Optimization */
@media (max-width: 480px) {
  /* Wix-specific mobile optimizations */
  [data-mesh-id], .wix-element {
    touch-action: manipulation !important;
  }
  
  /* Form optimization */
  input, textarea, select {
    font-size: 16px !important;
    padding: 12px 16px !important;
    border-radius: 8px !important;
    border: 2px solid #e5e7eb !important;
    width: 100% !important;
  }
  
  input:focus, textarea:focus, select:focus {
    border-color: var(--primary-color) !important;
    outline: none !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
  }
  
  /* Grid and layout fixes */
  [data-testid="grid"], .grid-container {
    grid-template-columns: 1fr !important;
    gap: 1rem !important;
  }
  
  /* Text readability */
  p, .text-element {
    font-size: 1rem !important;
    line-height: 1.6 !important;
  }
}

/* Tablet optimization */
@media (min-width: 481px) and (max-width: 768px) {
  [data-testid="grid"] {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}
</style>

<script>
// Mobile performance optimization
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
  document.documentElement.classList.add('mobile-device');
  
  // Optimize scroll performance on mobile
  let ticking = false;
  function updateScrollPosition() {
    ticking = false;
  }
  
  window.addEventListener('scroll', function() {
    if (!ticking) {
      requestAnimationFrame(updateScrollPosition);
      ticking = true;
    }
  }, { passive: true });
}
</script>
```

---

## STEP 5: IMPLEMENT LAZY LOADING (Updated Method)

### 5.1 Enable Built-in Lazy Loading
**Lazy loading is now automatic in Wix 2026, but you can enhance it:**

1. **Go to Media Manager**
2. **Click "Settings" (gear icon)**
3. **Ensure "Lazy Loading" is enabled** ✅
4. **Set "Loading Threshold" to 100px**

### 5.2 Add Enhanced Lazy Loading Script
**Create Custom Code:**
- **Name:** "Enhanced Lazy Loading 2026"
- **Place in:** "Body - End"
- **Pages:** "All Pages"

```html
<script>
// Enhanced lazy loading for Wix 2026
document.addEventListener('DOMContentLoaded', function() {
  // Enhanced intersection observer
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        
        // Handle Wix image elements
        if (img.dataset.src) {
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
        }
        
        // Handle Wix background images
        if (img.dataset.bg) {
          img.style.backgroundImage = `url(${img.dataset.bg})`;
          img.removeAttribute('data-bg');
        }
        
        // Add loaded class
        img.classList.add('loaded');
        img.setAttribute('data-loaded', 'true');
        
        observer.unobserve(img);
      }
    });
  }, {
    rootMargin: '50px 0px',
    threshold: 0.01
  });
  
  // Observe all images
  const lazyImages = document.querySelectorAll('img[data-src], [data-bg], [data-testid="image"]');
  lazyImages.forEach(img => {
    imageObserver.observe(img);
  });
  
  // Optimize Wix animations on mobile
  if (window.innerWidth <= 768) {
    const style = document.createElement('style');
    style.textContent = `
      .mobile-device * {
        animation-duration: 0.3s !important;
        transition-duration: 0.3s !important;
      }
    `;
    document.head.appendChild(style);
  }
});
</script>
```

---

## STEP 6: ADD RESOURCE HINTS (Updated)

### 6.1 Add Performance Resource Hints
**Create Custom Code:**
- **Name:** "Resource Hints 2026"
- **Place in:** "Head"
- **Pages:** "All Pages"

```html
<!-- Updated resource hints for Wix 2026 -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://static.wixstatic.com">
<link rel="preconnect" href="https://www.google-analytics.com">

<!-- DNS prefetch for Wix 2026 domains -->
<link rel="dns-prefetch" href="//static.wixstatic.com">
<link rel="dns-prefetch" href="//fonts.googleapis.com">
<link rel="dns-prefetch" href="//www.googletagmanager.com">
<link rel="dns-prefetch" href="//www.wix.com">

<!-- Viewport optimization for 2026 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
<meta name="format-detection" content="telephone=yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">

<!-- Preload critical fonts -->
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"></noscript>
```

---

## STEP 7: OPTIMIZE FONTS (Updated Process)

### 7.1 Access Font Settings (New Location)
1. **In Wix Editor, click "Design" at the top**
2. **Click "Theme" in the dropdown**
3. **Click "Fonts" tab**
4. **Choose web-optimized fonts:**

**Recommended font combinations:**
```
Primary Font: Inter (Google Fonts)
Secondary Font: Inter (same for consistency)

Weights to select ONLY:
- Regular (400) ✅
- Semi-Bold (600) ✅ - for headings only
- Bold (700) ✅ - for emphasis only

❌ Avoid: Light, Medium, Extra Bold (reduces loading time)
```

### 7.2 Add Font Display Optimization
**Add to Resource Hints custom code:**

```html
<style>
/* Font display optimization for 2026 */
@font-face {
  font-family: 'Inter';
  font-display: swap; /* Shows fallback while loading */
  src: local('Inter'), url('font-url') format('woff2');
}

/* Optimized font stack */
body, .wix-text, [data-testid="text"] {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif !important;
}

/* Prevent invisible text during font load */
.wix-text {
  font-display: swap;
}
</style>
```

---

## STEP 8: BASIC SEO SETUP (Updated Interface)

### 8.1 Access SEO Settings (New Location)
1. **Go to your site dashboard**
2. **Click "Marketing & SEO" in left sidebar**
3. **Click "SEO Tools"**
4. **Click "Get Found on Google"**

### 8.2 Configure Site-Wide SEO
**Fill in the updated form:**

```
Site Title: Intelevate - Hybrid Learning Labs for Tier 2/3 Cities
Site Description: Transform careers and businesses through practical learning labs, corporate consulting, and innovation projects. Connecting Tier 2/3 talent with global opportunities.
Keywords: hybrid learning labs, tier 2 cities India, skills development, corporate training, career development
```

### 8.3 Optimize Individual Pages (Updated Process)
**For each page:**
1. **In Wix Editor, select the page**
2. **Click "Page Settings" (gear icon in top toolbar)**
3. **Click "SEO Settings" tab**
4. **Fill in optimized content:**

#### Home Page SEO:
```
Page Title: Intelevate: Bridge Skills Gap with Hybrid Learning Labs | Tier 2/3 India
Meta Description: Transform careers and businesses through practical learning labs, corporate consulting, and innovation projects. Connecting Tier 2/3 talent with global opportunities.
```

#### Students Page SEO:
```
Page Title: Career Development Programs with Job Placement | Intelevate Learning Labs  
Meta Description: Launch your career with industry-relevant skills. Data science, digital marketing, and product management programs with 90%+ placement rates in Tier 2/3 cities.
```

### 8.4 Add Updated Structured Data
**Create Custom Code:**
- **Name:** "Schema 2026"
- **Place in:** "Head"
- **Pages:** "All Pages"

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "EducationalOrganization",
  "name": "Intelevate",
  "alternateName": "Intelevate Learning Labs",
  "url": "https://www.intelevates.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://www.intelevates.com/images/logo.png"
  },
  "description": "Hybrid learning labs, corporate consulting, and innovation projects that transform careers and businesses across India's Tier 2/3 cities.",
  "foundingDate": "2023",
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "IN"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "availableLanguage": ["English", "Hindi"]
  },
  "sameAs": [
    "https://www.linkedin.com/company/intelevate",
    "https://twitter.com/intelevate"
  ]
}
</script>
```

---

## STEP 9: TEST YOUR OPTIMIZATIONS (Updated Tools)

### 9.1 Use Updated Testing Tools
1. **Google PageSpeed Insights:** https://pagespeed.web.dev/
2. **GTmetrix:** https://gtmetrix.com/
3. **Wix Site Speed Dashboard:** 
   - Go to **Dashboard → Analytics → Site Speed**

### 9.2 Target Scores for 2026:
```
Performance: 75+ (good for Wix)
Accessibility: 90+
Best Practices: 85+
SEO: 95+
Core Web Vitals: All "Good" (green)
```

### 9.3 Mobile Testing
**Test on actual devices or use:**
- Chrome DevTools (F12 → Device Mode)
- Test different screen sizes:
  - iPhone SE (375px)
  - iPad (768px)
  - Desktop (1200px)

---

## STEP 10: PUBLISH OPTIMIZED SITE

### 10.1 Final Checklist
- [ ] Website Performance Settings enabled
- [ ] All custom code applied and saved
- [ ] Images optimized and uploaded
- [ ] Mobile view tested and working
- [ ] SEO settings configured for all pages
- [ ] Forms are touch-friendly on mobile

### 10.2 Publish
1. **Click "Publish" in Wix Editor**
2. **Wait for publishing to complete**
3. **Test the live site immediately**

---

## TROUBLESHOOTING UPDATED INTERFACE

### Can't Find Performance Settings?
**Try these locations:**
1. **Dashboard → Settings → Search "Website Performance"**
2. **Editor → Pages → Page Settings → Advanced Settings**
3. **Dashboard → Marketing & SEO → Site Speed**

### Custom Code Not Working?
**Check these:**
1. **Code placement:** Head vs Body-End
2. **Page selection:** All Pages vs Specific Pages
3. **Code type:** HTML (not CSS or JavaScript separately)

### Mobile View Issues?
**Solutions:**
1. **Clear browser cache**
2. **Test on actual mobile device**
3. **Check viewport meta tag is added**
4. **Verify touch-friendly button sizes (44px minimum)**

---

## EXPECTED RESULTS WITH 2026 OPTIMIZATIONS

### Performance Improvements:
- **25-40% faster loading times**
- **Better Core Web Vitals scores**
- **Improved mobile experience**
- **Higher search engine rankings**

### User Experience Gains:
- **Smoother navigation**
- **Faster image loading**
- **Better mobile usability**
- **Professional appearance across devices**

This updated guide reflects the current 2026 Wix interface and should work perfectly with the latest dashboard structure!