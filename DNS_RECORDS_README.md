# 🌐 DNS_RECORDS_README.md — VelNexis Domain DNS Setup

> **Purpose:** Domain khareedne ke BAAD ye records apne DNS provider ke panel mein
> MANUALLY add karni hain. (Koi external DNS operation yahan se perform NAHI hua —
> ye file sirf exact, copy-paste-ready values deti hai.)
>
> **Domain (planned):** `velnexis.com`
> **DNS provider:** jahan se domain khareedo ge (Cloudflare recommended)

---

## PART 1 — Website records (pehle ye lagao)

Netlify → **Domain management → Add domain** karte waqt Netlify khud exact values
dikhata hai. Reference ke liye standard Netlify values:

| Type | Name/Host | Value | TTL |
|---|---|---|---|
| A | `@` | `75.2.60.5` | Auto |
| CNAME | `www` | `velnexis.netlify.app` | Auto |

⚠️ Netlify ka panel jo bole wahi final hai — agar values alag hon to Netlify wali use karo.

---

## PART 2 — SPF record (email spoofing lock)

VelNexis abhi apne domain se **koi email send nahi karti** — is liye sab se
secure SPF "koi bhi mail qabol nahi" wali hai:

| Field | Value |
|---|---|
| Type | `TXT` |
| Name/Host | `@` |
| Value | `v=spf1 -all` |
| TTL | Auto |

**Agar baad mein Cloudflare Email Forwarding on karo** (info@velnexis.com → Gmail):

```
v=spf1 include:_spf.mx.cloudflare.net -all
```

**Agar baad mein Google Workspace lo** (proper business email):

```
v=spf1 include:_spf.google.com -all
```

---

## PART 3 — DMARC record

| Field | Value |
|---|---|
| Type | `TXT` |
| Name/Host | `_dmarc` |
| Value (abhi, email send nahi hota) | `v=DMARC1; p=reject; adkim=s; aspf=s;` |
| TTL | Auto |

**Agar email forwarding/Workspace on ho** to ye use karo (`YOUR-EMAIL` ki jagah
apni woh email likho jo DMARC reports receive kare — reports mein kaun fake mail
bhej raha hai wo aata hai):

```
v=DMARC1; p=quarantine; rua=mailto:YOUR-EMAIL
```

---

## Order of operations (5 steps)

1. **Domain kharido** (Cloudflare ~$9.15/saal ya local registrar ~Rs 3,000-3,500)
2. **Netlify → VelNexis project → Domain management → Add domain** → `velnexis.com`
3. DNS provider mein **PART 1** ke website records lagao
4. Phir **PART 2 + PART 3** ke TXT records lagao (SPF + DMARC)
5. **Verify:** mxtoolbox.com pe jao → domain daalo → SPF + DMARC dona green hon chahiye
   (DNS lagne mein 5 min – 1 ghanta lag sakta hai)

---

## Ek baar domain lag jaye to (mujhe ya admin se karna)

- `/admin` → Site Settings → **Site URL** → `https://velnexis.com` (canonical/sitemap
  khud update ho jayenge)
- Search Console mein property add karo + `sitemap.xml` submit karo

*File version: Sep 2026 — VelNexis project documentation.*
