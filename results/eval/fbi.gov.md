# OSINT briefing — `fbi.gov`

- **Generated:** 2026-05-05T07:18:39+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 76.58 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
**fbi.gov** – the primary domain of the United States Federal Bureau of Investigation.

## Key facts
- **Domain registration**: Registered through **get.gov** on **1997‑10‑02** and set to expire on **2026‑08‑21** (WHOIS).  
- **Name servers**: Hosted on Google Cloud DNS – `ns-cloud-e1.googledomains.com` through `ns-cloud-e4.googledomains.com` (WHOIS, DNS NS).  
- **IP addresses**: Resolves to **104.16.149.244** and **104.16.148.244** (IPv4) and to **2606:4700::6810:95f4** / **2606:4700::6810:94f4** (IPv6) (DNS A/AAAA).  
- **Mail exchangers**: Two MX records – `mx-east.fbi.gov` (priority 10) and `mx-west.fbi.gov` (priority 20) (DNS MX).  
- **Service exposure**: Shodan reports open ports 80, 443, 2082‑2087, 2095, 8080, 8443, 8880 on the primary IP (Shodan). The host is identified as **fbi.gov** and runs Cloudflare (`cpe:/a:cloudflare:cloudflare`) (Shodan).  
- **Historical snapshots**: First archived capture on **1996‑10‑22**, last on **2002‑09‑14**, with a total of **200** snapshots (Wayback).

## Notable findings
- **Multiple verification TXT records**: The zone contains a variety of verification strings for Google, Apple, Amazon SES, Adobe, GlobalSign, and Microsoft (`google-site-verification`, `apple-domain-verification`, `amazonses`, `MS=ms39271050`, etc.) (DNS TXT).  
- **SPF policy**: `v=spf1 +mx ip4:153.31.0.0/16 -all` indicates mail is permitted from the domain’s MX hosts and the 153.31.0.0/16 network (DNS TXT).  
- **Fastly delegation record**: `fastly-domain-delegation-weownfbi.gov-273985-2020-08-06` suggests use of Fastly CDN for some sub‑services (DNS TXT).  
- **Presence of uncommon ports** (2082‑2087, 2095, 8080, 8443, 8880) may indicate auxiliary web‑hosting or management interfaces behind Cloudflare (Shodan).

## Open questions
- What services are bound to the non‑standard ports (2082‑2087, 2095, 8080, 8443, 8880) and are they publicly accessible or restricted?  
- How are the various third‑party verification records (Google, Apple, Amazon SES, Adobe, GlobalSign) currently used—are they tied to active services or legacy configurations?  
- Is the SPF‑declared IP range (153.31.0.0/16) still in active use for outbound mail, and does it align with the observed MX hosts?  

*All statements are directly derived from the provided WHOIS, DNS, Shodan, and Wayback evidence.*

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 8 |
| DNS | 1 | 23 |
| Shodan IDB | 1 | 12 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 3 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `get.gov` | WHOIS |
| 2 | whois | creation_date | `1997-10-02` | WHOIS |
| 3 | whois | expiration_date | `2026-08-21` | WHOIS |
| 4 | whois | name_server | `ns-cloud-e1.googledomains.com` | WHOIS |
| 5 | whois | name_server | `ns-cloud-e2.googledomains.com` | WHOIS |
| 6 | whois | name_server | `ns-cloud-e3.googledomains.com` | WHOIS |
| 7 | whois | name_server | `ns-cloud-e4.googledomains.com` | WHOIS |
| 8 | whois | registrant_org | `REDACTED FOR PRIVACY` | WHOIS |
| 9 | dns | dns.a | `104.16.149.244` | DNS A |
| 10 | dns | dns.a | `104.16.148.244` | DNS A |
| 11 | dns | dns.aaaa | `2606:4700::6810:95f4` | DNS AAAA |
| 12 | dns | dns.aaaa | `2606:4700::6810:94f4` | DNS AAAA |
| 13 | dns | dns.mx | `10 mx-east.fbi.gov.` | DNS MX |
| 14 | dns | dns.mx | `20 mx-west.fbi.gov.` | DNS MX |
| 15 | dns | dns.ns | `ns-cloud-e3.googledomains.com.` | DNS NS |
| 16 | dns | dns.ns | `ns-cloud-e4.googledomains.com.` | DNS NS |
| 17 | dns | dns.ns | `ns-cloud-e1.googledomains.com.` | DNS NS |
| 18 | dns | dns.ns | `ns-cloud-e2.googledomains.com.` | DNS NS |
| 19 | dns | dns.txt | `fastly-domain-delegation-weownfbi.gov-273985-2020-08-06` | DNS TXT |
| 20 | dns | dns.txt | `8OOn7pVOB40yx/xtV+rLeDEYiUCieNfF7XI2xMbcm8t8PfUvZsCwGxmvHu2DLsMUkZ6UTYUvIJ49EPi3` | DNS TXT |
| 21 | dns | dns.txt | `_globalsign-domain-verification=xZMJnzdDAgURaBjUZ6qbqWaaYmV5W3sfo3TF8mUxne` | DNS TXT |
| 22 | dns | dns.txt | `625558384-8740534` | DNS TXT |
| 23 | dns | dns.txt | `apple-domain-verification=oOspXl6Jvnx9HzLM` | DNS TXT |
| 24 | dns | dns.txt | `amazonses: iUbfpGEqhMPlcmJ0aykJZREltK6pWio9wOgRngnJOQE=` | DNS TXT |
| 25 | dns | dns.txt | `google-site-verification=uTH4Vg-Xcc9hTqSdeThbT9UnYvuphObtVSpCEgaGr78` | DNS TXT |
| 26 | dns | dns.txt | `MS=ms39271050` | DNS TXT |
| 27 | dns | dns.txt | `google-site-verification=L8cauHJF4MANoTCkMbrLkAVfHBta28ctva9n1IDekTo` | DNS TXT |
| 28 | dns | dns.txt | `google-site-verification=6UEk-jfg1xPNjz_rQGcRFJOBGxMy1aARDZUTXgSNAqw` | DNS TXT |
| 29 | dns | dns.txt | `v=spf1 +mx ip4:153.31.0.0/16 -all` | DNS TXT |
| 30 | dns | dns.txt | `adobe-idp-site-verification=101945e35b37c6efd526cf706f04bc9545a02f9cdc58dbf71867` | DNS TXT |
| 31 | dns | dns.txt | `ublrZj1CzpSEiwtiRFKDAyiek8hRqkqaTTApxvhwai14i8JqVBOauW4cA06i39H5Lhl3HnALCM/xfTxI` | DNS TXT |
| 32 | shodan | open_port | `80` | https://internetdb.shodan.io/104.16.148.244 |
| 33 | shodan | open_port | `443` | https://internetdb.shodan.io/104.16.148.244 |
| 34 | shodan | open_port | `2082` | https://internetdb.shodan.io/104.16.148.244 |
| 35 | shodan | open_port | `2083` | https://internetdb.shodan.io/104.16.148.244 |
| 36 | shodan | open_port | `2086` | https://internetdb.shodan.io/104.16.148.244 |
| 37 | shodan | open_port | `2087` | https://internetdb.shodan.io/104.16.148.244 |
| 38 | shodan | open_port | `2095` | https://internetdb.shodan.io/104.16.148.244 |
| 39 | shodan | open_port | `8080` | https://internetdb.shodan.io/104.16.148.244 |
| 40 | shodan | open_port | `8443` | https://internetdb.shodan.io/104.16.148.244 |
| 41 | shodan | open_port | `8880` | https://internetdb.shodan.io/104.16.148.244 |
| 42 | shodan | hostname | `fbi.gov` | https://internetdb.shodan.io/104.16.148.244 |
| 43 | shodan | cpe | `cpe:/a:cloudflare:cloudflare` | https://internetdb.shodan.io/104.16.148.244 |
| 44 | wayback | wayback.first_snapshot | `1996-10-22` | https://web.archive.org/web/19961022175021/http://www.fbi.gov:80/ |
| 45 | wayback | wayback.last_snapshot | `2002-09-14` | https://web.archive.org/web/20020914012833/http://www2.fbi.gov:80/ |
| 46 | wayback | wayback.snapshot_count | `200` | http://web.archive.org/cdx/search/cdx |

## Trace

- plan: First run whois to capture registrar details, creation/expiry dates and name‑servers, establishing ownership and infrastructure age. Next query dns for A/AAAA, MX, NS, TXT and CNAME records to map current hosts, mail routing and any SPF/DKIM policies. Then pull Shodan InternetDB data to see open ports, services, hostnames and known vulnerabilities tied to those IPs. After that search GitHub for the domain to spot accidental commits exposing configs or credentials. Finally review Wayback snapshots to track historical site changes, subdomains and legacy content.
- decide -> whois: Start with cheap WHOIS lookup to get registrar and ownership details
- observe: whois: 8 findings (8 new), elapsed 1065 ms
- decide -> dns: Gather current DNS records to map hosts, mail routing, and security policies
- observe: dns: 23 findings (23 new), elapsed 1465 ms
- decide -> shodan: Gather open ports, services and vulnerabilities for fbi.gov IPs
- observe: shodan: 12 findings (12 new), elapsed 624 ms
- decide -> github: Next tool in plan is GitHub to find any accidental commits or exposed configs for fbi.gov
- observe: github: 0 findings (0 new), elapsed 3275 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to gather historical snapshots of fbi.gov
- observe: wayback: 3 findings (3 new), elapsed 4311 ms
- decide -> stop: All tools have been used and evidence gathered
