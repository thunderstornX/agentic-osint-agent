# OSINT briefing — `berkeley.edu`

- **Generated:** 2026-05-05T07:23:34+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 70.55 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
**berkeley.edu** – primary domain of the University of California, Berkeley.

## Key facts
- Authoritative A records resolve to two IPv4 addresses: **141.193.213.20** and **141.193.213.21** (dns)  
- Nameservers are **adns1.berkeley.edu**, **adns2.berkeley.edu**, **adns3.berkeley.edu** (dns)  
- Mail is handled by Google Workspace (MX records pointing to `aspmx.l.google.com` and its alternates) (dns)  
- SPF TXT record includes multiple third‑party services (`_spf.berkeley.edu`, `_spf2.berkeley.edu`, Google, Qualtrics, Mailchimp, Mailjet, Service‑Now) (dns)  
- Numerous verification TXT records are present for services such as iContact, Brevo, Klaviyo, Microsoft, Amazon SES, Zoom, Autodesk, Jamf, Atlassian, Adobe, Apple, and Docusign (dns)  

## Notable findings
- **Open ports on 141.193.213.21** (Shodan) include standard web ports **80** and **443**, plus a range of control‑panel ports (2052‑2053, 2082‑2083, 2086‑2087, 2095‑2096, 8080, 8443, 8880) (shodan).  
- The Shodan fingerprint identifies the host as running **Cloudflare** (`cpe:/a:cloudflare:cloudflare`) (shodan).  
- Shodan also reports two hostnames associated with the same IP: **qrm.leeds.ac.uk** and **wpewaf.com** (shodan).  

## Open questions
- What services are bound to the non‑standard ports (e.g., 2052, 2082, 8443) on 141.193.213.21?  
- Why does the same IP host external hostnames (`qrm.leeds.ac.uk`, `wpewaf.com`) – is this a shared Cloudflare edge node or a misconfiguration?  
- Are any of the listed verification TXT records (e.g., for Zoom, Autodesk, Jamf) actively used by the university, or are they remnants of past integrations?  

*All statements are directly derived from the provided DNS, WHOIS, and Shodan evidence.*

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 0 |
| DNS | 1 | 37 |
| Shodan IDB | 1 | 16 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | dns | dns.a | `141.193.213.20` | DNS A |
| 2 | dns | dns.a | `141.193.213.21` | DNS A |
| 3 | dns | dns.mx | `1 aspmx.l.google.com.` | DNS MX |
| 4 | dns | dns.mx | `5 alt2.aspmx.l.google.com.` | DNS MX |
| 5 | dns | dns.mx | `10 alt3.aspmx.l.google.com.` | DNS MX |
| 6 | dns | dns.mx | `10 alt4.aspmx.l.google.com.` | DNS MX |
| 7 | dns | dns.mx | `5 alt1.aspmx.l.google.com.` | DNS MX |
| 8 | dns | dns.ns | `adns1.berkeley.edu.` | DNS NS |
| 9 | dns | dns.ns | `adns2.berkeley.edu.` | DNS NS |
| 10 | dns | dns.ns | `adns3.berkeley.edu.` | DNS NS |
| 11 | dns | dns.txt | `v=spf1 include:_spf.berkeley.edu include:_spf2.berkeley.edu include:_spf.google.` | DNS TXT |
| 12 | dns | dns.txt | `iContact1462072` | DNS TXT |
| 13 | dns | dns.txt | `brevo-code:e1e8345a4a2352cdbd9d6979093f2aec` | DNS TXT |
| 14 | dns | dns.txt | `klaviyo-site-verification=SWYLuM` | DNS TXT |
| 15 | dns | dns.txt | `MS=10BE0CF63C8BD5AFF9A6EF7B71763B098A905719` | DNS TXT |
| 16 | dns | dns.txt | `docusign=31f4475e-737f-4a3a-b6ea-60b1ac273c95` | DNS TXT |
| 17 | dns | dns.txt | `google-site-verification=CDuttEoV44OF0dD7qwidnTj3wvYxIPz05W6MKEZfKYc` | DNS TXT |
| 18 | dns | dns.txt | `brevo-code:ee0b01818d57850991280d3999efc841` | DNS TXT |
| 19 | dns | dns.txt | `brevo-code:a2b2aef0282cf9caec92be7bed7630ad` | DNS TXT |
| 20 | dns | dns.txt | `MS=ms37758698` | DNS TXT |
| 21 | dns | dns.txt | `MS=ms19521665` | DNS TXT |
| 22 | dns | dns.txt | `amazonses:IuakF7FVH1Y7h0Kap7krqHwRvoXFOzSET+Ri1VBHziA=` | DNS TXT |
| 23 | dns | dns.txt | `google-site-verification=fL93jj-VPnl_5wdFDh26YshzKVPraWAurHaBCu-k-Xw` | DNS TXT |
| 24 | dns | dns.txt | `896263912-18360412` | DNS TXT |
| 25 | dns | dns.txt | `iContact1583632` | DNS TXT |
| 26 | dns | dns.txt | `ZOOM_verify_RirbP7N1QWC3Zzm02oL4Cw` | DNS TXT |
| 27 | dns | dns.txt | `autodesk-domain-verification=ccDWtL-BsuXH4WkjoUiP` | DNS TXT |
| 28 | dns | dns.txt | `google-site-verification=loQrJWyMsMB249uINb-AsRGTWVoLdTc44Td3aMGn-NE` | DNS TXT |
| 29 | dns | dns.txt | `docusign=25bb9bc1-b377-48ce-a907-61472fca6261` | DNS TXT |
| 30 | dns | dns.txt | `google-site-verification=C4YkQW0t-gtD5FpVWdjxAipEUofVb2p0KmW3xFaUJeA` | DNS TXT |
| 31 | dns | dns.txt | `iContact1393487` | DNS TXT |
| 32 | dns | dns.txt | `jamf-site-verification=2jicltwxCxH93ep4OhO0dA` | DNS TXT |
| 33 | dns | dns.txt | `google-site-verification=R5hbazPMfJqtXtm6OHprlDpBnSThQvYDrt-i-IqZvjE` | DNS TXT |
| 34 | dns | dns.txt | `sending_domain102272=da1fdb1bce80fcb235c498ec3ad47745fed6ea7c6dc03752d88318531e6` | DNS TXT |
| 35 | dns | dns.txt | `apple-domain-verification=ZDtApcKYPmKfYxn4` | DNS TXT |
| 36 | dns | dns.txt | `atlassian-domain-verification=RIwGoMGAwFoHKm3AJg0bhFvuzEkRseqI6LStzthTqt4dWfA6Mq` | DNS TXT |
| 37 | dns | dns.txt | `adobe-idp-site-verification=a113c870-3c49-4b4a-b3a4-31e1cf1860cb` | DNS TXT |
| 38 | shodan | open_port | `80` | https://internetdb.shodan.io/141.193.213.21 |
| 39 | shodan | open_port | `443` | https://internetdb.shodan.io/141.193.213.21 |
| 40 | shodan | open_port | `2052` | https://internetdb.shodan.io/141.193.213.21 |
| 41 | shodan | open_port | `2053` | https://internetdb.shodan.io/141.193.213.21 |
| 42 | shodan | open_port | `2082` | https://internetdb.shodan.io/141.193.213.21 |
| 43 | shodan | open_port | `2083` | https://internetdb.shodan.io/141.193.213.21 |
| 44 | shodan | open_port | `2086` | https://internetdb.shodan.io/141.193.213.21 |
| 45 | shodan | open_port | `2087` | https://internetdb.shodan.io/141.193.213.21 |
| 46 | shodan | open_port | `2095` | https://internetdb.shodan.io/141.193.213.21 |
| 47 | shodan | open_port | `2096` | https://internetdb.shodan.io/141.193.213.21 |
| 48 | shodan | open_port | `8080` | https://internetdb.shodan.io/141.193.213.21 |
| 49 | shodan | open_port | `8443` | https://internetdb.shodan.io/141.193.213.21 |
| 50 | shodan | open_port | `8880` | https://internetdb.shodan.io/141.193.213.21 |
| 51 | shodan | hostname | `qrm.leeds.ac.uk` | https://internetdb.shodan.io/141.193.213.21 |
| 52 | shodan | hostname | `wpewaf.com` | https://internetdb.shodan.io/141.193.213.21 |
| 53 | shodan | cpe | `cpe:/a:cloudflare:cloudflare` | https://internetdb.shodan.io/141.193.213.21 |

## Trace

- plan: First run whois to capture registrar details, creation/expiry dates and name‑servers, establishing ownership and infrastructure baseline. Next query dns to list A/AAAA, MX, NS, TXT and CNAME records, revealing current services, mail routing and possible subdomains. Then use shodan to pull InternetDB data for those IPs, exposing open ports, hostnames and known vulnerabilities. After that search github for “berkeley.edu” in code, hunting accidental credential leaks or internal URLs. Finally check wayback to view historic snapshots, tracking domain changes, old subdomains and deprecated services.
- decide -> whois: Start with cheap WHOIS lookup to get registrar and ownership details
- observe: whois: 0 findings (0 new), elapsed 423 ms
- decide -> dns: Gather DNS records to map the domain's infrastructure before deeper probing
- observe: dns: 37 findings (37 new), elapsed 3147 ms
- decide -> shodan: Next step is to query Shodan for the IPs discovered to reveal open ports and services
- observe: shodan: 16 findings (16 new), elapsed 413 ms
- decide -> github: Search code repositories for references to berkeley.edu to find leaks or internal URLs
- observe: github: 0 findings (0 new), elapsed 3055 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to gather historic domain snapshots
- observe: wayback: 0 findings (0 new), elapsed 15351 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All five tools have been used and evidence gathered
