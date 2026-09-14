# 🔑 VelNexis — WordPress-Style Admin Panel Setup (ZERO Coding)

## Yeh kya hai?

Aapki site pe ek **secret dashboard** lagega: `velnexis.netlify.app/admin` — wahan se aap **bilkul WordPress ki tarah**:
- 📝 Naye articles likho/publish karo (visual editor — WhatsApp web jaisa typing)
- ✏️ Purane articles ka naam ya text badlo → **Publish → 1-2 minute mein site live update**
- 📚 Nayi categories banao (form bharo — review box khud ban jayega)
- ⚙️ Site ka naam, hero text, trust points — sab forms se badlo
- 📄 About/Privacy/Terms pages edit karo

**Koi coding nahi. Koi command nahi. Sirf click aur type.**

> Main ne saari technical files pehle hi bana di hain (`admin/` folder + `netlify.toml`). Aapko bas neeche ke steps karne hain — sirf **ek baar**, setup ke liye.

---

## 📋 SETUP — sirf ek baar (15-20 minute)

### Step 1: GitHub pe account + code upload (5 min)
1. **GitHub.com** kholo → **Sign up** (email + password) → email verify karo
2. Login ke baad upar right **+** → **New repository**
3. Naam likho: `velnexis` → **Private** select karo → **Create repository**
4. Nayi page pe likha hoga *"uploading an existing file"* — us **uploading an existing file** link pe click karo
5. Apne computer pe `velnexis` folder kholo → **andar ki SAARI cheezein select karo** (content, assets, admin folders + build.py, netlify.toml, index.html waghera) → browser ke upload box mein **drag & drop** karo
6. **Commit changes** button dabao (neeche green button) — wait till upload completes

⚠️ Folder ke andar ki cheezein upload karo, folder khud nahi (taake GitHub pe `content/` root mein ho, `velnexis/content/` nahi)

### Step 2: Netlify pe site live karo (5 min)
1. **Netlify.com** → **Sign up** → **GitHub se login** karo (jo Step 1 mein banaya)
2. Login ke baad: **Add new site → Import an existing project**
3. **GitHub** select karo → **Authorize** → `velnexis` repo pe click karo
4. Settings khud milengi (build command `netlify.toml` se parh liya) → **Deploy**
5. 2-3 minute wait → site live: `kuch-bhi.netlify.app` 🎉 (Site settings → Change site name → `velnexis`)

### Step 3: Admin panel ON karo (5 min)
1. Netlify mein site kholo → **Site settings → Identity** → **Enable Identity**
2. Wahi Identity page pe: **Registration** → **Invite only** select karo (taake koi ajnabi sign up na kar sake)
3. **Integrations tab → Identity → Git Gateway → Enable Git Gateway** (permissions default chhor do)
4. Identity page pe **Invite members** → **apna email likho** → invite
5. Apna email kholo → Netlify ka email aayega → link pe click → **password bana lo**

### Step 4: Login karo! 🎉
1. `velnexis.netlify.app/admin` kholo (apna site naam)
2. **Login with Netlify** → email + password
3. Dashboard khul gaya: **📝 Articles · 📚 Categories · 📄 Pages · ⚙️ Site Settings**

---

## ✍️ Ab rozana kaam kaise karte hain (10 second ka process)

**Naya article:**
Articles → **+ New** → Title likho → Category chuno → bade box mein article type karo (upar toolbar mein **B** bold, bullet, heading buttons — MS Word jaisa) → **Save** → **Publish** ✅

**Article edit:**
Articles → list mein article pe click → type kar ke theek karo → **Publish** ✅ (1-2 min mein live)

**Article ka naam change:** wahi editor mein Title box badlo → Publish

**Nayi category:** Categories → + New → Naam, icon (emoji), color (# hex), rating, verdict, pros/cons likho → Publish → category page + review box khud ban gaya

**Site ka text (hero waghera):** Site Settings → Main Settings → jo badalna hai badlo → Publish

> Har Publish ke baad Netlify khud site rebuild karta hai — 1-2 minute mein live. Kuch bhi install ya command nahi chalana.

---

## 🌐 Apna domain (velnexis.com) — jab chaho
Netlify → Site settings → **Domain management** → Add domain → `velnexis.com` → jo 2 DNS records batayenge woh domain company (Namecheap waghera) ke DNS settings mein paste karo → free SSL automatic. Free SSL included.

---

## 🆘 Masail aur hal

| Masla | Hal |
|---|---|
| `/admin` khulta hai lekin login ke baad error | Netlify → Integrations → Git Gateway enable hai? Identity → Registration "Invite only" hai? |
| Publish kiya lekin site update nahi hui | 2 minute wait karo; Netlify → Deploys mein check karo green tick aaya? |
| Article mein link dena hai | Editor mein text select karo → link button 🔗 → jaise `articles/wifi-disconnects` likho (sirf article ka naam, .html ke bina nahi to .md bhi chalega) |
| Naya category option article mein nahi dikh raha | Admin Categories mein banana parega pehle; ya article mein cat khud type kar do — lekin behtar hai pehle category banao |
| Galti se kuch delete ho gaya | GitHub repo → har save ki purani version wapas milta hai (History) |

---

## 📌 Yaad rakhne wali 3 baatein
1. **Local files aur GitHub dono zinda hain** — admin panel GitHub ko edit karta hai, wahan se site banti hai. Aapke computer wali folder ab sirf backup hai
2. **Images:** article mein photo lagani ho to editor ka 🖼 image button use karo (ya pehle assets/uploads mein upload kar ke link do)
3. **AdSense:** jab 20-30 articles ho jayen, tab apply karo — process `deploy-guide.md` mein hai
