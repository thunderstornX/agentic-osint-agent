# OSINT briefing — `cloudflare.com`

- **Generated:** 2026-05-05T07:28:22+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 80.28 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
**cloudflare.com** – domain registered to Cloudflare, Inc.

## Key facts
- **Registrar & registration**: Cloudflare, Inc. (WHOIS). Domain created 2009‑02‑17, expires 2033‑02‑17 (WHOIS).  
- **Name servers**: ns3‑ns7.cloudflare.com (WHOIS & DNS NS).  
- **IP addresses**: 104.16.133.229, 104.16.132.229 (DNS A); IPv6 2606:4700::6810:85e5, 2606:4700::6810:84e5 (DNS AAAA).  
- **Mail routing**: MX records point to `mxa‑canary.global.inbound.cf-emailsecurity.net`, `mxb‑canary.global.inbound.cf-emailsecurity.net`, `mxa.global.inbound.cf-emailsecurity.net`, `mxb.global.inbound.cf-emailsecurity.net` (DNS MX).  
- **SPF**: Includes Cloudflare‑owned IP ranges and several third‑party services (Google, Mandrill, Zendesk, Salesforce, etc.) (DNS TXT).  
- **Service verification TXT records**: Numerous vendor‑verification strings (Apple, Google, Atlassian, Zoom, Canva, Uber, Docker, Facebook, Stripe, Cisco, Microsoft, etc.) (DNS TXT).  

## Notable findings
- **Open ports** on the primary IP (104.16.132.229) include standard web ports 80/443 and a range of cPanel/WHM ports (2082‑2087, 2095‑2096, 8080, 8443, 8880) (Shodan).  
- **Shodan hostnames** associated with the IP: `cloudflare.com`, `secondary.cloudflare.com`, `ns.cloudflare.com` (Shodan).  
- **CPE identifier** confirms the service as Cloudflare software (`cpe:/a:cloudflare:cloudflare`) (Shodan).  
- **Historical snapshots**: First archived capture 2009‑09‑01, last 2012‑11‑01, with ~200 snapshots total (Wayback).  

## Open questions
- Why are cPanel/WHM ports (2082‑2087, 2095‑2096, etc.) exposed on a Cloudflare front‑end IP?  
- Are the numerous vendor verification TXT records actively used for domain ownership proofs, or are they remnants?  
- No evidence of recent Wayback snapshots beyond 2012; what changes have occurred on the site since then?  

*All statements are directly drawn from the provided WHOIS, DNS, Shodan, and Wayback evidence.*

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 9 |
| DNS | 1 | 39 |
| Shodan IDB | 1 | 15 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 3 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `Cloudflare, Inc.` | WHOIS |
| 2 | whois | creation_date | `2009-02-17` | WHOIS |
| 3 | whois | expiration_date | `2033-02-17` | WHOIS |
| 4 | whois | name_server | `ns3.cloudflare.com` | WHOIS |
| 5 | whois | name_server | `ns4.cloudflare.com` | WHOIS |
| 6 | whois | name_server | `ns5.cloudflare.com` | WHOIS |
| 7 | whois | name_server | `ns6.cloudflare.com` | WHOIS |
| 8 | whois | name_server | `ns7.cloudflare.com` | WHOIS |
| 9 | whois | registrant_org | `DATA REDACTED` | WHOIS |
| 10 | dns | dns.a | `104.16.133.229` | DNS A |
| 11 | dns | dns.a | `104.16.132.229` | DNS A |
| 12 | dns | dns.aaaa | `2606:4700::6810:85e5` | DNS AAAA |
| 13 | dns | dns.aaaa | `2606:4700::6810:84e5` | DNS AAAA |
| 14 | dns | dns.mx | `5 mxa-canary.global.inbound.cf-emailsecurity.net.` | DNS MX |
| 15 | dns | dns.mx | `5 mxb-canary.global.inbound.cf-emailsecurity.net.` | DNS MX |
| 16 | dns | dns.mx | `10 mxa.global.inbound.cf-emailsecurity.net.` | DNS MX |
| 17 | dns | dns.mx | `10 mxb.global.inbound.cf-emailsecurity.net.` | DNS MX |
| 18 | dns | dns.ns | `ns6.cloudflare.com.` | DNS NS |
| 19 | dns | dns.ns | `ns4.cloudflare.com.` | DNS NS |
| 20 | dns | dns.ns | `ns7.cloudflare.com.` | DNS NS |
| 21 | dns | dns.ns | `ns3.cloudflare.com.` | DNS NS |
| 22 | dns | dns.ns | `ns5.cloudflare.com.` | DNS NS |
| 23 | dns | dns.txt | `miro-verification=bdd7dfa0a49adfb43ad6ddfaf797633246c07356` | DNS TXT |
| 24 | dns | dns.txt | `v=spf1 ip4:199.15.212.0/22 ip4:173.245.48.0/20 include:_spf.google.com include:s` | DNS TXT |
| 25 | dns | dns.txt | `apple-domain-verification=DNnWJoArJobFJKhJ` | DNS TXT |
| 26 | dns | dns.txt | `google-site-verification=ZdlQZLBBAPkxeFTCM1rpiB_ibtGff_JF5KllNKwDR9I` | DNS TXT |
| 27 | dns | dns.txt | `atlassian-domain-verification=WxxKyN9aLnjEsoOjUYI6T0bb5vcqmKzaIkC9Rx2QkNb751G3LL` | DNS TXT |
| 28 | dns | dns.txt | `ZOOM_verify_7LFBvOO9SIigypFG2xRlMA` | DNS TXT |
| 29 | dns | dns.txt | `canva-site-verification=oOyaVnHC-OiFoR1BPvetNA` | DNS TXT |
| 30 | dns | dns.txt | `creatopy-domain-verification=97d2ca50-9b6f-4a21-9bdb-fbb630e4cec7` | DNS TXT |
| 31 | dns | dns.txt | `google-site-verification=C7thfNeXVahkVhniiqTI1iSVnElKR_kBBtnEHkeGDlo` | DNS TXT |
| 32 | dns | dns.txt | `uber-domain-verification=58086039-150a-42a4-a4be-b4032921aa0f` | DNS TXT |
| 33 | dns | dns.txt | `docker-verification=c578e21c-34fb-4474-9b90-d55ee4cba10c` | DNS TXT |
| 34 | dns | dns.txt | `_neqmkgaq1lq9it5s8qmetrhbnu121wb` | DNS TXT |
| 35 | dns | dns.txt | `facebook-domain-verification=h9mm6zopj6p2po54woa16m5bskm6oo` | DNS TXT |
| 36 | dns | dns.txt | `status-page-domain-verification=r14frwljwbxs` | DNS TXT |
| 37 | dns | dns.txt | `drift-domain-verification=f037808a26ae8b25bc13b1f1f2b4c3e0f78c03e67f24cefdd4ec52` | DNS TXT |
| 38 | dns | dns.txt | `onetrust-domain-verification=bd5cd08a1e9644799fdb98ed7d60c9cb` | DNS TXT |
| 39 | dns | dns.txt | `stripe-verification=bf1a94e6b16ace2502a4a7fff574a25c8a45291054960c883c59be39d178` | DNS TXT |
| 40 | dns | dns.txt | `asv=894f6d1f9f83bcf44e4b1bc40bc1c4aa` | DNS TXT |
| 41 | dns | dns.txt | `_saml-domain-challenge.2dc00405-79cd-457b-b288-a119c6f0c7b7.71996d53-d178-4ba9-b` | DNS TXT |
| 42 | dns | dns.txt | `cisco-ci-domain-verification=27e926884619804ef987ae4aa1c4168f6b152ada84f4c8bfc74` | DNS TXT |
| 43 | dns | dns.txt | `_wkjc0fot0d7qrvrdt78bxkj2e2o67d2` | DNS TXT |
| 44 | dns | dns.txt | `MS=ms70274184` | DNS TXT |
| 45 | dns | dns.txt | `liveramp-site-verification=EhH1MqgwbndTWl1AN64hOTKz7hc1s80yUpchLbgpfY0` | DNS TXT |
| 46 | dns | dns.txt | `databank-domain-verification-hkehd2=fzgu4kmbZwMoW99zENgO4u8NL` | DNS TXT |
| 47 | dns | dns.txt | `logmein-verification-code=b3433c86-3823-4808-8a7e-58042469f654` | DNS TXT |
| 48 | dns | dns.txt | `stripe-verification=5096d01ff2cf194285dd51cae18f24fa9c26dc928cebac3636d462b4c692` | DNS TXT |
| 49 | shodan | open_port | `80` | https://internetdb.shodan.io/104.16.132.229 |
| 50 | shodan | open_port | `443` | https://internetdb.shodan.io/104.16.132.229 |
| 51 | shodan | open_port | `2082` | https://internetdb.shodan.io/104.16.132.229 |
| 52 | shodan | open_port | `2083` | https://internetdb.shodan.io/104.16.132.229 |
| 53 | shodan | open_port | `2086` | https://internetdb.shodan.io/104.16.132.229 |
| 54 | shodan | open_port | `2087` | https://internetdb.shodan.io/104.16.132.229 |
| 55 | shodan | open_port | `2095` | https://internetdb.shodan.io/104.16.132.229 |
| 56 | shodan | open_port | `2096` | https://internetdb.shodan.io/104.16.132.229 |
| 57 | shodan | open_port | `8080` | https://internetdb.shodan.io/104.16.132.229 |
| 58 | shodan | open_port | `8443` | https://internetdb.shodan.io/104.16.132.229 |
| 59 | shodan | open_port | `8880` | https://internetdb.shodan.io/104.16.132.229 |
| 60 | shodan | hostname | `cloudflare.com` | https://internetdb.shodan.io/104.16.132.229 |
| 61 | shodan | hostname | `secondary.cloudflare.com` | https://internetdb.shodan.io/104.16.132.229 |
| 62 | shodan | hostname | `ns.cloudflare.com` | https://internetdb.shodan.io/104.16.132.229 |
| 63 | shodan | cpe | `cpe:/a:cloudflare:cloudflare` | https://internetdb.shodan.io/104.16.132.229 |
| 64 | wayback | wayback.first_snapshot | `2009-09-01` | https://web.archive.org/web/20090901035818/http://www.cloudflare.com:80/ |
| 65 | wayback | wayback.last_snapshot | `2012-11-01` | https://web.archive.org/web/20121101160121/https://www.cloudflare.com/ |
| 66 | wayback | wayback.snapshot_count | `200` | http://web.archive.org/cdx/search/cdx |

## Trace

- plan: First run whois to capture the registrar, registration dates and name‑servers, establishing ownership and infrastructure baseline. Next query dns for A/AAAA, MX, NS, TXT and CNAME records to map current services, mail routing and any hidden subdomains. Then use shodan to discover open ports, hostnames and known vulnerabilities on the resolved IPs. After that search github for “cloudflare.com” code‑dorks to find accidental credential or config leaks. Finally pull wayback snapshots to see historical DNS, site content and subdomain changes over time.
- decide -> whois: Start with the cheapest tool to gather registration and ownership details for cloudflare.com
- observe: whois: 9 findings (9 new), elapsed 639 ms
- decide -> dns: Gather current DNS records to map services and subdomains after establishing WHOIS info
- observe: dns: 39 findings (39 new), elapsed 447 ms
- decide -> shodan: Next step is to discover open ports, hostnames, and vulnerabilities on cloudflare.com IPs
- observe: shodan: 15 findings (15 new), elapsed 536 ms
- decide -> github: Next tool in plan to search for code leaks related to cloudflare.com
- observe: github: 0 findings (0 new), elapsed 2912 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Retrieve historical snapshots to see past DNS, site content, and subdomain changes
- observe: wayback: 3 findings (3 new), elapsed 13554 ms
- decide -> stop: All five tools have been used and evidence gathered
