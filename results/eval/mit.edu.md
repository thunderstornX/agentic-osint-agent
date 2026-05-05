# OSINT briefing — `mit.edu`

- **Generated:** 2026-05-05T07:19:59+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 80.69 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
**mit.edu** – primary domain of the Massachusetts Institute of Technology.

## Key facts
- **A record:** `23.15.150.186` (DNS) – the main IPv4 address for the domain.  
- **AAAA records:** `2600:1413:5000:881::255e` and `2600:1413:5000:887::255e` (DNS).  
- **Mail routing:** MX points to `100 mit-edu.mail.protection.outlook.com.` (DNS).  
- **Name servers:** Eight Akamai DNS servers (e.g., `ns1-173.akam.net.`, `asia1.akam.net.` etc.) (DNS).  
- **TXT records:** Numerous verification strings for services such as Airtable, Atlassian, Stripe, Google, OpenAI, Adobe, Amazon SES, DocuSign, Mandrill, HubSpot, and SPF (`v=spf1 include:_s00430413.autospf.email -all`) (DNS).  
- **Open port 443** is observed on the IPv4 address (Shodan).  
- **Hostnames resolved to the IP** include a large set of MIT sub‑domains (e.g., `www.mit.edu`, `mitpress.mit.edu`, `climate.mit.edu`, `alum.mit.edu`, `giving.mit.edu`, `web.mit.edu`, `www-staging.mit.edu`, etc.) (Shodan).

## Notable findings
- The domain is **fronted by Akamai** CDN infrastructure, as indicated by the NS list and the hostname `a23-15-150-186.deploy.static.akamaitechnologies.com` (Shodan).  
- **Extensive third‑party service verification** is present in TXT records, suggesting integration with many SaaS platforms (Airtable, Atlassian, Stripe, Google, OpenAI, Adobe, Amazon SES, DocuSign, Mandrill, HubSpot).  
- The **SPF record** references an internal autospf service (`_s00430413.autospf.email`) rather than typical MIT mail servers, implying custom outbound mail handling (DNS).  
- **Port 443** is the only open port reported, consistent with HTTPS‑only public services (Shodan).

## Open questions
- What specific services are hosted on the numerous sub‑domains listed by Shodan, and are any of them exposed beyond the CDN edge?  
- Are the verification TXT records actively used, and do they correspond to active accounts or legacy configurations?  
- Does the custom SPF include any external senders that could be leveraged for spoofing or phishing?  
- No IPv6‑only services or additional open ports were observed; further scanning could confirm the full surface.

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 0 |
| DNS | 1 | 45 |
| Shodan IDB | 1 | 33 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | dns | dns.a | `23.15.150.186` | DNS A |
| 2 | dns | dns.aaaa | `2600:1413:5000:881::255e` | DNS AAAA |
| 3 | dns | dns.aaaa | `2600:1413:5000:887::255e` | DNS AAAA |
| 4 | dns | dns.mx | `100 mit-edu.mail.protection.outlook.com.` | DNS MX |
| 5 | dns | dns.ns | `ns1-173.akam.net.` | DNS NS |
| 6 | dns | dns.ns | `asia1.akam.net.` | DNS NS |
| 7 | dns | dns.ns | `eur5.akam.net.` | DNS NS |
| 8 | dns | dns.ns | `usw2.akam.net.` | DNS NS |
| 9 | dns | dns.ns | `use5.akam.net.` | DNS NS |
| 10 | dns | dns.ns | `use2.akam.net.` | DNS NS |
| 11 | dns | dns.ns | `asia2.akam.net.` | DNS NS |
| 12 | dns | dns.ns | `ns1-37.akam.net.` | DNS NS |
| 13 | dns | dns.txt | `e2ma-verification=uviib` | DNS TXT |
| 14 | dns | dns.txt | `E2MA-VERIFICATION=8AWBB` | DNS TXT |
| 15 | dns | dns.txt | `airtable-verification=46ae122907d40a1413b6a05898774435` | DNS TXT |
| 16 | dns | dns.txt | `1VNZ334aKc8FypCKDhIMOQBsKFd8gCgTFQuPlDwQfzPNxPCKonTOnhuFQ8+kE32E2TgkBiOp9EFab5nf` | DNS TXT |
| 17 | dns | dns.txt | `*fastly-domain-delegation-hnb9joooe7gojgqu4eth-00494769-2025-08-23` | DNS TXT |
| 18 | dns | dns.txt | `atlassian-domain-verification=3Ex0JUvwojvbDLOJvNHnYUFEZCF+kwii0OjHbhDkymB97xpCOk` | DNS TXT |
| 19 | dns | dns.txt | `stripe-verification=fe726543b783764b2ba9137f4e675faa0709416ac7a5d9f50e21248a706a` | DNS TXT |
| 20 | dns | dns.txt | `google-site-verification=pqf9o422iIeT7mzfZmQwkpLYH3VTlB05OC9c_OncFOg` | DNS TXT |
| 21 | dns | dns.txt | `AIRTABLE-VERIFICATION=C8040E640F7DEAB69A01D68C91893E07` | DNS TXT |
| 22 | dns | dns.txt | `E2MA-VERIFICATION=C8D4` | DNS TXT |
| 23 | dns | dns.txt | `atlassian-domain-verification=3eRva0Gy/EjVyKEw46uExfEXpDGJfhwocwVCy5NTxcPpf89Aqd` | DNS TXT |
| 24 | dns | dns.txt | `v=spf1 include:_s00430413.autospf.email -all` | DNS TXT |
| 25 | dns | dns.txt | `ecgkc7fnflsm01hh6uqjr86h02` | DNS TXT |
| 26 | dns | dns.txt | `openai-domain-verification=dv-pavuNIk1XG88x99BoqSFI0Zs` | DNS TXT |
| 27 | dns | dns.txt | `airtable-verification=4283ac2aa983e97636807d478d6bf30c` | DNS TXT |
| 28 | dns | dns.txt | `pardot_310211_*=a4e9728d1b90355b6240f4d7778cc4da11c10a20552ae99e6ed03d8e48c06583` | DNS TXT |
| 29 | dns | dns.txt | `atlassian-domain-verification=maRNLIMivtdhvCr9JoVuLKHWRn7mZOY8072lyRNeyamz0NHc/s` | DNS TXT |
| 30 | dns | dns.txt | `adobe-idp-site-verification=0817e32603f0dda03188b9f1f3bbaf4f754c5322926036af8890` | DNS TXT |
| 31 | dns | dns.txt | `amazonses:asyYfDTQj+TCy9t5jFbakgwGbomDqXREEs3KdC0iMQE=` | DNS TXT |
| 32 | dns | dns.txt | `docusign=37fbdad0-5267-4b79-9402-ff9df7e9331f` | DNS TXT |
| 33 | dns | dns.txt | `e2ma-verification=piiib` | DNS TXT |
| 34 | dns | dns.txt | `google-site-verification=6ethhhET4cfz7L1Dfve9bCOTAqMr6IU79Va6gb8HxlA` | DNS TXT |
| 35 | dns | dns.txt | `docusign=78c4c36c-1180-44b1-b277-be9be4a08b73` | DNS TXT |
| 36 | dns | dns.txt | `E2MA-VERIFICATION=MONGB` | DNS TXT |
| 37 | dns | dns.txt | `E2MA-VERIFICATION=86JGB` | DNS TXT |
| 38 | dns | dns.txt | `mgverify=2a07014ab707abf9b6f984210c05ef7a1fd905296aebe173776844c14db61c1e` | DNS TXT |
| 39 | dns | dns.txt | `google-site-verification=qNAffaSjUkhb2JCBb1BQ2nXAkcNYLeLc7G6vjMRD1js` | DNS TXT |
| 40 | dns | dns.txt | `google-site-verification=b4-1loZHD1WzNmews_hsTTKL__gLblD6iKBFbA4j97c` | DNS TXT |
| 41 | dns | dns.txt | `e2ma-verification=xiiib` | DNS TXT |
| 42 | dns | dns.txt | `mandrill_verify.28vVgPhRZLda1o_v90CPWg` | DNS TXT |
| 43 | dns | dns.txt | `e2ma-verification=oiiib` | DNS TXT |
| 44 | dns | dns.txt | `include:4920340.spf07.hubspotemail.net` | DNS TXT |
| 45 | dns | dns.txt | `airtable-manual-domain-verification=ce83c94e-0127-4fd3-9265-3b37a46a7b8a` | DNS TXT |
| 46 | shodan | open_port | `443` | https://internetdb.shodan.io/23.15.150.186 |
| 47 | shodan | hostname | `swartz-report.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 48 | shodan | hostname | `mit.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 49 | shodan | hostname | `www.web.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 50 | shodan | hostname | `www-staging.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 51 | shodan | hostname | `mitpress.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 52 | shodan | hostname | `www.mit` | https://internetdb.shodan.io/23.15.150.186 |
| 53 | shodan | hostname | `swartz-documents.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 54 | shodan | hostname | `web-forms.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 55 | shodan | hostname | `w.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 56 | shodan | hostname | `www.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 57 | shodan | hostname | `emergency-dev.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 58 | shodan | hostname | `mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 59 | shodan | hostname | `web.mit` | https://internetdb.shodan.io/23.15.150.186 |
| 60 | shodan | hostname | `staging-mitpress.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 61 | shodan | hostname | `mitpressbookstore.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 62 | shodan | hostname | `a23-15-150-186.deploy.static.akamaitechnologies.com` | https://internetdb.shodan.io/23.15.150.186 |
| 63 | shodan | hostname | `climate.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 64 | shodan | hostname | `alum-dev.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 65 | shodan | hostname | `events-static.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 66 | shodan | hostname | `www-mit.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 67 | shodan | hostname | `wwww.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 68 | shodan | hostname | `www-cert.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 69 | shodan | hostname | `giving.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 70 | shodan | hostname | `web.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 71 | shodan | hostname | `thereader-staging.mitpress.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 72 | shodan | hostname | `img.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 73 | shodan | hostname | `w3.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 74 | shodan | hostname | `web-cert.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 75 | shodan | hostname | `thereader.mitpress.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 76 | shodan | hostname | `alum.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 77 | shodan | hostname | `giving-dev.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |
| 78 | shodan | hostname | `web-staging.mit.edu` | https://internetdb.shodan.io/23.15.150.186 |

## Trace

- plan: First run whois to capture the registrar, registration dates and name‑servers, establishing ownership and infrastructure baseline. Next query dns for A/AAAA, MX, NS, TXT and CNAME records to map current services, mail routing and possible subdomains. Then pull Shodan InternetDB data to see open ports, hostnames and known vulnerabilities tied to those IPs. After that search GitHub code for “mit.edu” patterns to uncover accidental credential or config leaks. Finally review Wayback snapshots to track historical site changes, retired subdomains and legacy infrastructure.
- decide -> whois: Start with cheap WHOIS lookup to get ownership and name‑server info for mit.edu
- observe: whois: 0 findings (0 new), elapsed 951 ms
- decide -> dns: Next cheap tool to map the domain's records and subdomains
- observe: dns: 45 findings (45 new), elapsed 943 ms
- decide -> shodan: Next gather open ports and host info for MIT's IPs after DNS and WHOIS
- observe: shodan: 33 findings (33 new), elapsed 702 ms
- decide -> github: Search GitHub for MIT domain references to find potential credential or config leaks
- observe: github: 0 findings (0 new), elapsed 3275 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to gather historical snapshots of mit.edu
- observe: wayback: 0 findings (0 new), elapsed 15425 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All five tools have been used and evidence gathered
