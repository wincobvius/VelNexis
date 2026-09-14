# 🚀 VelNexis — Live Karne Ki Complete Guide (Roman Urdu)

---

## 🛣️ 2 Raste hain — pehle faisla kar lo:

| | **Raasta A: Static Hosting** | **Raasta B: WordPress** |
|---|---|---|
| Cost | **FREE** (Netlify/Cloudflare Pages) | Hosting ~Rs.1,000/mah + Domain ~Rs.3,500/saal |
| Time | 10 minute | 1-2 ghante |
| Content add karna | `build.py` + coding wala tareeqa | Dashboard se bilkul asaan (mobile se bhi) |
| Plugins (SEO, forms, ads) | Nahi milte | Milte hain |
| Kis ke liye best | Jaldi live + test + sasti shuruaat | Long-term + AdSense serious earning |
| AdSense | Chalega (custom domain ke sath) | Chalega (zyada comfortable) |

**Meri recommendation:** Pehle **Raasta A** se free live kar lo (aaj hi), phir jab traffic aana shuru ho to **Raasta B (WordPress)** pe shift kar lo. Dono mein domain (velnexis.com) same rehta hai — koi cheez waste nahi hoti.

---

## 🅰️ RAASTA A — Free Static Hosting (Netlify) — 10 Minute

1. **Netlify.com** pe jao → **Sign up** (Google account se free)
2. Login ke baad: **Add new site → Deploy manually**
3. Apne computer pe `velnexis` folder ko zip kar ke **drag & drop** kar do
4. **Bas — site live ho gayi!** `kuch-bhi.netlify.app` address milega
5. Site name change karo: **Site settings → Change site name** → `velnexis` likho → ab mila `velnexis.netlify.app`
6. (Behtar) **Custom domain:** velnexis.com kharido (Namecheap ~$10/saal) → Netlify → Domain settings → Add domain → jo DNS records batayenge woh Namecheap mein daal do → free SSL automatic

✅ Free SSL (https), fast CDN, koi bandwidth charge nahi
✅ Update karna: `build.py` se pages regenerate karo → Netlify pe folder dobara drag & drop — 30 second mein live update

---

## 🅱️ RAASTA B — WordPress Deployment (Detail)

### Step 0 — Kharidari
1. **Domain:** velnexis.com — Namecheap/GoDaddy/Hostinger se (~$10-12/saal)
2. **Hosting:** Hostinger Premium ya Namecheap Stellar — WordPress support wali (Linux hosting)
3. Domain ko hosting se **connect** karo (nameservers change — hosting company steps batati hai)

### Step 1 — WordPress Install
- Hosting ke control panel (hPanel/cPanel) → **Auto Installer / Softaculous** → WordPress → install
- Login: `velnexis.com/wp-admin`

### Step 2 — Bunyadi Settings
- **Settings → Permalinks → "Post name"** select karo (SEO ke liye zaroori)
- Settings → General → site title: **VelNexis**, tagline: *Tech Truth, Tips & Trends*

### Step 3 — Theme
- **Appearance → Themes → Add New → "Astra"** install + activate (free, fast)
- Astra mein colors set karo: background **#090810**, text **#ECEAE6**, accent purple **#8B5CF6**
- (Global colors option se ek jagah set karo, sab jagah apply ho jata hai)

### Step 4 — VelNexis ki CSS lagao
- **Appearance → Customize → Additional CSS** kholo
- Main jo `wordpress-css.css` file dunga uska content paste kar do → Publish
- Poori site ka dark look, cards, buttons, fonts — sab apply ho jayega

### Step 5 — Fonts
- Plugin install karo: **OMGF** (free) → isme Google Fonts add karo: **Inter** (400/500/700/800) + **Newsreader Italic 300-600**
- Ya Additional CSS mein: `@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&family=Newsreader:ital,opsz,wght@1,6..72,300..600&display=swap');`

### Step 6 — Pages + Categories
- **Pages → Add New:** Home, About Us, Contact Us, Privacy Policy, Terms & Conditions, Disclaimer
- Har page ke liye main **WordPress-ready content files** dunga — editor mein **Custom HTML block** add kar ke paste karo (simple copy-paste)
- **Posts → Categories:** 8 categories banao (AI & Rumor Checks, Gaming, Windows Issues, Android Issues, Privacy & Hacking, How-To Guides, Reviews, Tech News) + har ek ki description

### Step 7 — Articles
- **Posts → Add New** → title, category select, content paste (Custom HTML block), excerpt field mein summary
- Rank Math seo title/description khud suggest karega

### Step 8 — Homepage
- **Settings → Reading → A static page → Homepage: Home** select karo

### Step 9 — Menu
- **Appearance → Menus → Create Menu** → Home, About, Contact, Privacy Policy add karo + Categories ko auto-add karo
- Location: **Primary Menu** assign karo

### Step 10 — Plugins (sab free)
| Plugin | Kaam |
|---|---|
| **Rank Math SEO** | SEO + sitemap (khud banata hai) |
| **WPForms Lite** | Contact form (real emails bhejta hai) |
| **LiteSpeed Cache** | Speed (Hostinger pe) / WP Super Cache |
| **Insert Headers and Footers** | Baad mein AdSense code ke liye |
| **Easy Table of Contents** | Lambi articles mein TOC |

### Step 11 — Contact Form
- WPForms → Simple Contact Form banao → Contact page mein block se embed karo

### Step 12 — Google Search Console
- [search.google.com/search-console](https://search.google.com/search-console) → property add karo → verify
- Sitemap submit karo: `velnexis.com/sitemap_index.xml` (Rank Math banata hai)

### Step 13 — AdSense (LAST — sab ke baad)
1. Kam se kam **20-30 original articles** + 2-4 hafte regular posting
2. [adsense.google.com](https://adsense.google.com) → Apply → site URL + payment info
3. Approval ke **baad** hi ads lagao (Insert Headers and Footers mein code)
4. `ads.txt` file hosting pe upload karo (AdSense khud batata hai)

---

## ⚠️ Common Ghaltiyan (bach ke raho)
- ❌ Free wordpress.com subdomain se AdSense apply karna (reject hota hai)
- ❌ Design live hone se **pehle** hi AdSense apply kar dena (pehle content poora karo)
- ❌ HTML pages ko WordPress mein aise paste karna ke nav/footer bhi double ho jaye — content files sirf **body content** rakhti hain
- ❌ Google Images se photos uthana — sirf Pexels/Unsplash/Pixabay

---

## 📦 Main kya files bana sakta hoon (bolo to):
1. `wordpress-css.css` — Additional CSS ke liye ready
2. Har page ka **WordPress-ready content** (Custom HTML block mein paste karne wala, bina nav/footer)
3. Har article ka post content + excerpt + category — ready-to-paste
4. Category descriptions (SEO wali)
