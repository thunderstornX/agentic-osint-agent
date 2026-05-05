# OSINT briefing — `wikipedia.org`

- **Generated:** 2026-05-05T07:30:33+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 62.15 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
**wikipedia.org** – the primary domain of the free encyclopedia project.

## Key facts
- Registered with **MarkMonitor Inc.** on 13 Jan 2001, expiring 13 Jan 2027. (WHOIS)  
- Authoritative name servers: **ns0.wikimedia.org**, **ns1.wikimedia.org**, **ns2.wikimedia.org**. (WHOIS / DNS NS)  
- Resolves to **IPv4 103.102.166.224** and **IPv6 2001:df2:e500:ed1a::1**. (DNS A, DNS AAAA)  
- Mail exchangers: **mx‑in1001.wikimedia.org**, **mx‑in2001.wikimedia.org** (priority 10). (DNS MX)  
- SPF record: `v=spf1 include:_cidrs.wikimedia.org ~all`. (DNS TXT)  
- Verification TXT records for Google and Yandex. (DNS TXT)  

## Notable findings
- Shodan reports port **443** open on the IP address, confirming HTTPS service. (Shodan)  
- The same IP hosts a large set of Wikimedia‑related hostnames (e.g., **wikivoyage.org**, **wikinews.org**, **wikidata.org**, **mediawiki.org**, **wmfusercontent.org**, etc.), indicating shared infrastructure across the Wikimedia ecosystem. (Shodan)  
- Wayback Machine shows the domain’s earliest archived snapshot on **27 Jul 2001** and a later snapshot on **30 Jul 2005**, with a total of **≈200** snapshots captured between those dates. (Wayback)  

## Open questions
- The evidence does not reveal any additional IP addresses, CDN usage, or load‑balancing details beyond the single IPv4/IPv6 pair.  
- No information is available on current TLS certificate details, server software versions, or recent configuration changes.  
- Lack of recent Wayback snapshots after 2005 limits insight into the domain’s evolution in the past decade.  

*All statements are directly derived from the provided WHOIS, DNS, Shodan, and Wayback records.*

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 6 |
| DNS | 1 | 10 |
| Shodan IDB | 1 | 17 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 3 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `MarkMonitor Inc.` | WHOIS |
| 2 | whois | creation_date | `2001-01-13` | WHOIS |
| 3 | whois | expiration_date | `2027-01-13` | WHOIS |
| 4 | whois | name_server | `ns0.wikimedia.org` | WHOIS |
| 5 | whois | name_server | `ns1.wikimedia.org` | WHOIS |
| 6 | whois | name_server | `ns2.wikimedia.org` | WHOIS |
| 7 | dns | dns.a | `103.102.166.224` | DNS A |
| 8 | dns | dns.aaaa | `2001:df2:e500:ed1a::1` | DNS AAAA |
| 9 | dns | dns.mx | `10 mx-in1001.wikimedia.org.` | DNS MX |
| 10 | dns | dns.mx | `10 mx-in2001.wikimedia.org.` | DNS MX |
| 11 | dns | dns.ns | `ns2.wikimedia.org.` | DNS NS |
| 12 | dns | dns.ns | `ns0.wikimedia.org.` | DNS NS |
| 13 | dns | dns.ns | `ns1.wikimedia.org.` | DNS NS |
| 14 | dns | dns.txt | `v=spf1 include:_cidrs.wikimedia.org ~all` | DNS TXT |
| 15 | dns | dns.txt | `google-site-verification=AMHkgs-4ViEvIJf5znZle-BSE2EPNFqM1nDJGRyn2qk` | DNS TXT |
| 16 | dns | dns.txt | `yandex-verification: 35c08d23099dc863` | DNS TXT |
| 17 | shodan | open_port | `443` | https://internetdb.shodan.io/103.102.166.224 |
| 18 | shodan | hostname | `wikivoyage.org` | https://internetdb.shodan.io/103.102.166.224 |
| 19 | shodan | hostname | `wikipedia.org` | https://internetdb.shodan.io/103.102.166.224 |
| 20 | shodan | hostname | `wikisource.org` | https://internetdb.shodan.io/103.102.166.224 |
| 21 | shodan | hostname | `wikinews.org` | https://internetdb.shodan.io/103.102.166.224 |
| 22 | shodan | hostname | `wiktionary.org` | https://internetdb.shodan.io/103.102.166.224 |
| 23 | shodan | hostname | `wikimedia.org` | https://internetdb.shodan.io/103.102.166.224 |
| 24 | shodan | hostname | `wikiversity.org` | https://internetdb.shodan.io/103.102.166.224 |
| 25 | shodan | hostname | `w.wiki` | https://internetdb.shodan.io/103.102.166.224 |
| 26 | shodan | hostname | `text-lb.eqsin.wikimedia.org` | https://internetdb.shodan.io/103.102.166.224 |
| 27 | shodan | hostname | `wmfusercontent.org` | https://internetdb.shodan.io/103.102.166.224 |
| 28 | shodan | hostname | `mediawiki.org` | https://internetdb.shodan.io/103.102.166.224 |
| 29 | shodan | hostname | `wikidata.org` | https://internetdb.shodan.io/103.102.166.224 |
| 30 | shodan | hostname | `wikibooks.org` | https://internetdb.shodan.io/103.102.166.224 |
| 31 | shodan | hostname | `wikimediafoundation.org` | https://internetdb.shodan.io/103.102.166.224 |
| 32 | shodan | hostname | `wikifunctions.org` | https://internetdb.shodan.io/103.102.166.224 |
| 33 | shodan | hostname | `wikiquote.org` | https://internetdb.shodan.io/103.102.166.224 |
| 34 | wayback | wayback.first_snapshot | `2001-07-27` | https://web.archive.org/web/20010727112808/http://www.wikipedia.org:80/ |
| 35 | wayback | wayback.last_snapshot | `2005-07-30` | https://web.archive.org/web/20050730083423/http://www.wikipedia.org:80/ |
| 36 | wayback | wayback.snapshot_count | `200` | http://web.archive.org/cdx/search/cdx |

## Trace

- plan: First run whois to capture the registrar, registration dates and name‑servers, establishing ownership and infrastructure baseline. Next query dns for A/AAAA, MX, NS, TXT and CNAME records to map current services, mail routing and any hidden subdomains. Then use shodan to enumerate open ports, hostnames and known vulnerabilities on the resolved IPs. After that search github for “wikipedia.org” code‑dorks to find accidental credential or config leaks. Finally pull wayback snapshots to see historical DNS, site structure and past subdomains.
- decide -> whois: Start with cheap WHOIS lookup to get registrar and registration details for wikipedia.org
- observe: whois: 6 findings (6 new), elapsed 592 ms
- decide -> dns: Gather DNS records to map services and subdomains after establishing WHOIS info
- observe: dns: 10 findings (10 new), elapsed 922 ms
- decide -> shodan: Next step is to enumerate open ports, hostnames and vulnerabilities on Wikipedia's IPs
- observe: shodan: 17 findings (17 new), elapsed 714 ms
- decide -> github: Next tool in plan to search code for wikipedia.org references
- observe: github: 0 findings (0 new), elapsed 3276 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to gather historical snapshots and past subdomains
- observe: wayback: 3 findings (3 new), elapsed 6235 ms
- decide -> stop: All tools have been used and evidence gathered
