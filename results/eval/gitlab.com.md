# OSINT briefing — `gitlab.com`

- **Generated:** 2026-05-05T07:27:02+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 64.2 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
gitlab.com  

## Key facts
- Domain registered through **GANDI SAS** on 15 Jan 2004, expiring 15 Jan 2027 and listed to **GitLab Inc.** as registrant (WHOIS).  
- Authoritative name servers are **diva.ns.cloudflare.com** and **jermaine.ns.cloudflare.com** (WHOIS/DNS NS).  
- Resolves to IPv4 **172.65.251.78** and IPv6 **2606:4700:90:0:f22e:fbec:5bed:a9b9** (DNS A/AAAA).  
- Mail is handled by Google Workspace (MX records pointing to `aspmx.l.google.com` and its alternates) (DNS MX).  
- DNS TXT records contain numerous third‑party verification strings (Google, OneTrust, Stripe, Docusign, Uber, Zapier, OpenAI, Apple, Adobe, etc.) and an SPF policy that includes services such as Zendesk, Google, Mailgun, Salesforce, GitLab’s own sending IPs, and specific IP ranges (DNS TXT).  

## Notable findings
- **Cloudflare** is the front‑end CDN/hosting provider, confirmed by open ports 22, 80, 443 and a Cloudflare CPE identifier in Shodan (Shodan).  
- The presence of a **gitlab-pages-verification-code** TXT entry indicates use of GitLab Pages for custom domain verification (DNS TXT).  
- Multiple verification records suggest extensive integration with third‑party SaaS platforms (e.g., Stripe, Docusign, Uber, Zapier, OpenAI) for payment, e‑signature, automation, and AI services.  

## Open questions
- The Shodan data shows SSH (port 22) open on the front‑end IP; it is unclear whether this is a management interface or a mis‑exposed service.  
- No evidence in the provided rows details internal infrastructure, CDN edge locations, or any sub‑domain enumeration. Further probing would be needed to map the full attack surface.  

*All statements are derived solely from the supplied WHOIS, DNS, and Shodan evidence.*

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 6 |
| DNS | 1 | 38 |
| Shodan IDB | 1 | 4 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `GANDI SAS` | WHOIS |
| 2 | whois | creation_date | `2004-01-15` | WHOIS |
| 3 | whois | expiration_date | `2027-01-15` | WHOIS |
| 4 | whois | name_server | `diva.ns.cloudflare.com` | WHOIS |
| 5 | whois | name_server | `jermaine.ns.cloudflare.com` | WHOIS |
| 6 | whois | registrant_org | `GitLab Inc.` | WHOIS |
| 7 | dns | dns.a | `172.65.251.78` | DNS A |
| 8 | dns | dns.aaaa | `2606:4700:90:0:f22e:fbec:5bed:a9b9` | DNS AAAA |
| 9 | dns | dns.mx | `1 aspmx.l.google.com.` | DNS MX |
| 10 | dns | dns.mx | `5 alt2.aspmx.l.google.com.` | DNS MX |
| 11 | dns | dns.mx | `5 alt1.aspmx.l.google.com.` | DNS MX |
| 12 | dns | dns.mx | `10 alt4.aspmx.l.google.com.` | DNS MX |
| 13 | dns | dns.mx | `10 alt3.aspmx.l.google.com.` | DNS MX |
| 14 | dns | dns.ns | `jermaine.ns.cloudflare.com.` | DNS NS |
| 15 | dns | dns.ns | `diva.ns.cloudflare.com.` | DNS NS |
| 16 | dns | dns.txt | `google-site-verification=uT9dAMjaTlnkbC0VnN5flFWp0Bsze7zHObWjZwkd2p8` | DNS TXT |
| 17 | dns | dns.txt | `onetrust-domain-verification=84b59aa2659244d486b0b86f5db073dd` | DNS TXT |
| 18 | dns | dns.txt | `smartsheet-site-validation=wTADkxxpf97DU9ZxO4RuFpZJyRvP7MRm` | DNS TXT |
| 19 | dns | dns.txt | `MS=ms60523131` | DNS TXT |
| 20 | dns | dns.txt | `google-site-verification=iWR2UGQb3MvVY83zY47ZFrGFVFLG6ADfpjqchlQjnok` | DNS TXT |
| 21 | dns | dns.txt | `google-site-verification=6Cb3PPpoMp6-xRavXf2HZz03s7pplQeG5MiUaPGIu_Q` | DNS TXT |
| 22 | dns | dns.txt | `v=spf1 include:mail.zendesk.com include:_spf.google.com include:mktomail.com inc` | DNS TXT |
| 23 | dns | dns.txt | `asv=3f763643512ad5bdcc0d42caea1b3951` | DNS TXT |
| 24 | dns | dns.txt | `google-site-verification=QiG7NTIWpedorFi71mMN7OVe2Fo_yA6RclsxO8stOa8` | DNS TXT |
| 25 | dns | dns.txt | `stripe-verification=E331E16D59119AEFB547211475C2E225C1BF6EB8CB885D300536B2852EAD` | DNS TXT |
| 26 | dns | dns.txt | `onetrust-domain-verification=af5b5fda116e45a9b4c4abcd9e571923` | DNS TXT |
| 27 | dns | dns.txt | `mgverify=9549a96a4bc9886fbf483bcd56872eaf2b5b9e690d264024041cf446664cb114` | DNS TXT |
| 28 | dns | dns.txt | `MS=ms83893381` | DNS TXT |
| 29 | dns | dns.txt | `serval-domain-verification-rahzqw=w9adwbCM3CJ9BrXnAleSWuMqz` | DNS TXT |
| 30 | dns | dns.txt | `docusign=1a7d6818-2cf5-4956-a9fb-c3d2e9a578dd` | DNS TXT |
| 31 | dns | dns.txt | `uber-domain-verification=38ba2b7b-5ae3-4694-9701-086b20ea3d36` | DNS TXT |
| 32 | dns | dns.txt | `zapier-domain-verification-challenge=a1d665be-8176-4ada-9707-4332dfa7a2cc` | DNS TXT |
| 33 | dns | dns.txt | `google-site-verification=lnPjOx5EAxmESH8FSn4colWVMAxe18K4ZIopDB1IEDY` | DNS TXT |
| 34 | dns | dns.txt | `v=MCPv1; k=ed25519; p=MmZM6XexKcX4jiWqHtn3M0av9Q7HDmonAdP6PqktwX0=` | DNS TXT |
| 35 | dns | dns.txt | `drift-domain-verification=fa583cfff88c496bcc62651057550656a98ab3e689c314255a1a6a` | DNS TXT |
| 36 | dns | dns.txt | `openai-domain-verification=dv-Uq90dak9n7LidGh0WsdFOOUu` | DNS TXT |
| 37 | dns | dns.txt | `apple-domain-verification=UNUD9vY0Jp9z5TjO` | DNS TXT |
| 38 | dns | dns.txt | `adobe-idp-site-verification=5a5e001556a2c0595ed571d2a1f7b5f8a749a00742853e035eb9` | DNS TXT |
| 39 | dns | dns.txt | `gitlab-pages-verification-code=5228e61c992af7e65f5f5160f0587fb4` | DNS TXT |
| 40 | dns | dns.txt | `_globalsign-domain-verification=4azHJ7gL04Dr8r2VR0txu7OrWg7uZpU6v7LOHVP1b3` | DNS TXT |
| 41 | dns | dns.txt | `google-site-verification=vPPg6DGiVgf5vhzQg5zGISLao6-07-lVzzpqvmCFe5Y` | DNS TXT |
| 42 | dns | dns.txt | `google-site-verification=XDRo7LEOqv6OV0RfGDFh7G2XgpzdycygGJBqde334q4` | DNS TXT |
| 43 | dns | dns.txt | `jamf-site-verification=nRPNM9HJGzWzUkvBtgvBrg` | DNS TXT |
| 44 | dns | dns.txt | `mgverify=2dd945066758840fe3bfbd9ccf90e2c6000458f13345baa576338880dcc86658` | DNS TXT |
| 45 | shodan | open_port | `22` | https://internetdb.shodan.io/172.65.251.78 |
| 46 | shodan | open_port | `80` | https://internetdb.shodan.io/172.65.251.78 |
| 47 | shodan | open_port | `443` | https://internetdb.shodan.io/172.65.251.78 |
| 48 | shodan | cpe | `cpe:/a:cloudflare:cloudflare` | https://internetdb.shodan.io/172.65.251.78 |

## Trace

- plan: First run whois to capture the registrar, registration dates and name‑servers, establishing ownership and age. Next query dns to list A/AAAA, MX, NS, TXT and CNAME records, revealing the current infrastructure and any sub‑domains. Then use shodan to pull InternetDB data for open ports, hostnames and known vulnerabilities/CPEs on the resolved IPs. After that search github for accidental commits containing the domain to uncover internal URLs, API keys or config files. Finally check wayback to view historical snapshots of gitlab.com and its sub‑domains, spotting legacy services or past changes.
- decide -> whois: Start with the cheapest tool to gather registration and ownership details for gitlab.com
- observe: whois: 6 findings (6 new), elapsed 847 ms
- decide -> dns: Gather DNS records to map the domain's infrastructure and subdomains
- observe: dns: 38 findings (38 new), elapsed 300 ms
- decide -> shodan: Next cheap tool to gather open ports and host info for gitlab.com
- observe: shodan: 4 findings (4 new), elapsed 520 ms
- decide -> github: Next tool in plan to find accidental commits with the domain
- observe: github: 0 findings (0 new), elapsed 2984 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to gather historical snapshots of gitlab.com
- observe: wayback: 0 findings (0 new), elapsed 15448 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All five tools have been used and evidence gathered
