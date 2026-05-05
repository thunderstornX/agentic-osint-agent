# OSINT briefing — `stanford.edu`

- **Generated:** 2026-05-05T07:21:16+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 77.12 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target  
**stanford.edu** – primary domain of Stanford University.

## Key facts  
- **IP addresses** – A record points to `171.67.215.200` and AAAA record to `2607:f6d0:0:925a::ab43:d7c8` (dns).  
- **Mail routing** – Two MX records both priority 10 point to `mxa-00000d07.gslb.pphosted.com.` and `mxb-00000d07.gslb.pphosted.com.` (dns).  
- **Name servers** – Hosted on a mix of internal and third‑party servers: `ns5.dnsmadeeasy.com.`, `ns6.dnsmadeeasy.com.`, `ns7.dnsmadeeasy.com.` (dns) plus internal hosts `atalante.stanford.edu.`, `avallone.stanford.edu.`, `argus.stanford.edu.` (dns).  
- **SPF policy** – TXT record contains a large SPF string authorising many IP ranges and third‑party services (Google, Qualtrics, Outlook, etc.) and ends with `?all` (dns).  

## Notable findings  
- **Extensive verification TXT records** – The domain publishes dozens of verification strings for services such as Google (`google-site-verification=`), Sendinblue, Brevo, Airtable, Atlassian, Adobe, Notion, Jamf, Autodesk, Samsung, Pexip, OneTrust, Wiz, and many `e2ma-verification=` entries (dns). These indicate active use of a wide variety of SaaS platforms and email marketing tools.  
- **Multiple third‑party email services** – Besides Google Workspace (`_spf.google.com`), the SPF includes Qualtrics, Outlook (`spf.protection.outlook.com`), and a range of IP blocks that likely belong to SendGrid/Sendinblue and other bulk‑mail providers (dns).  
- **Hybrid DNS hosting** – Core DNS is delegated to DNS Made Easy (ns5‑ns7) while several sub‑domains are served by internal Stanford name servers, suggesting a split‑horizon configuration (dns).  

## Open questions  
- Which specific sub‑domains correspond to the internal name servers (`atalante`, `avallone`, `argus`)?  
- What services are associated with the numerous `e2ma-verification` tokens (Mailgun, SendGrid, etc.)?  
- Are any of the listed IP ranges in the SPF record external to Stanford’s network, and what traffic do they generate?  

*All statements are derived solely from the provided DNS evidence.*

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 0 |
| DNS | 1 | 105 |
| Shodan IDB | 1 | 6 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 3 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | dns | dns.a | `171.67.215.200` | DNS A |
| 2 | dns | dns.aaaa | `2607:f6d0:0:925a::ab43:d7c8` | DNS AAAA |
| 3 | dns | dns.mx | `10 mxa-00000d07.gslb.pphosted.com.` | DNS MX |
| 4 | dns | dns.mx | `10 mxb-00000d07.gslb.pphosted.com.` | DNS MX |
| 5 | dns | dns.ns | `ns6.dnsmadeeasy.com.` | DNS NS |
| 6 | dns | dns.ns | `atalante.stanford.edu.` | DNS NS |
| 7 | dns | dns.ns | `avallone.stanford.edu.` | DNS NS |
| 8 | dns | dns.ns | `ns5.dnsmadeeasy.com.` | DNS NS |
| 9 | dns | dns.ns | `ns7.dnsmadeeasy.com.` | DNS NS |
| 10 | dns | dns.ns | `argus.stanford.edu.` | DNS NS |
| 11 | dns | dns.txt | `e2ma-verification=8z0eb` | DNS TXT |
| 12 | dns | dns.txt | `stripe-verification=984c5a4eb98ae34bbaf60c12403c1d8889d4ad02b2dc672232a89b21f905` | DNS TXT |
| 13 | dns | dns.txt | `vmware-cloud-verification-2abfb849-6039-461b-aa8b-eee2629dd6e4` | DNS TXT |
| 14 | dns | dns.txt | `e2ma-verification=k4dgb` | DNS TXT |
| 15 | dns | dns.txt | `google-site-verification=bamHrkKBqpOQ8ouXQe0uFSuvVUFTB_TLju7gSCNq_Qw` | DNS TXT |
| 16 | dns | dns.txt | `google-site-verification=p4uNfSaD7rr13xbA1Q1yW6I0DckXOv1ujjc0FQGjGEM` | DNS TXT |
| 17 | dns | dns.txt | `TAILSCALE-scyG2dkta4GC30jIuPOW` | DNS TXT |
| 18 | dns | dns.txt | `brevo-code:97c04c03c676317dbc22a7ee103483a6` | DNS TXT |
| 19 | dns | dns.txt | `e2ma-verification=vaogb` | DNS TXT |
| 20 | dns | dns.txt | `mgverify=c7c142ba8b95199619ad561a75f165ad285c322b3892f9621c083b0293fd0da0` | DNS TXT |
| 21 | dns | dns.txt | `e2ma-verification=ey8eb` | DNS TXT |
| 22 | dns | dns.txt | `airtable-verification=6ae90a183923b17d9f1c76e90e31b4e4` | DNS TXT |
| 23 | dns | dns.txt | `blitz=mu-0e24b17b-23dce65a-c0b14b75-e742cd66` | DNS TXT |
| 24 | dns | dns.txt | `anthropic-domain-verification-rrhf1p=E3SBrctYaemDvHQIrJbKWafVN` | DNS TXT |
| 25 | dns | dns.txt | `airtable-verification=bf58597802ed6d32ee6bcb86a575a186` | DNS TXT |
| 26 | dns | dns.txt | `e2ma-verification=nbxfb-remove` | DNS TXT |
| 27 | dns | dns.txt | `google-site-verification=JM6F1JtgpITjPAatlXWl2mpzq_zobtnQEwKsbGA0DIk` | DNS TXT |
| 28 | dns | dns.txt | `e2ma-verification=nw5fb` | DNS TXT |
| 29 | dns | dns.txt | `detectify-verification=bc8e96f8fbf64ced057d0f44eff83381` | DNS TXT |
| 30 | dns | dns.txt | `airtable-verification=866b719f2d2dab4393f0a7eb83f4d8ba` | DNS TXT |
| 31 | dns | dns.txt | `00DVG000007nUP7=1TBVG0000000LkP` | DNS TXT |
| 32 | dns | dns.txt | `e2ma-verification=v4lgb` | DNS TXT |
| 33 | dns | dns.txt | `brevo-code:033215cd835c1e9ddc21dfb479c54b76` | DNS TXT |
| 34 | dns | dns.txt | `brevo-code:09357c2630559d902817770f34dbf0b1` | DNS TXT |
| 35 | dns | dns.txt | `e2ma-verification=qmrgb` | DNS TXT |
| 36 | dns | dns.txt | `e2ma-verification=6uqeb` | DNS TXT |
| 37 | dns | dns.txt | `airtable-verification=13ac52fb202035dbad35b0ab24e598b4` | DNS TXT |
| 38 | dns | dns.txt | `airtable-verification=7cdd67720483f4801fc65d998968476e` | DNS TXT |
| 39 | dns | dns.txt | `e2ma-verification=d1ueb` | DNS TXT |
| 40 | dns | dns.txt | `jamf-site-verification=YL4ixnZvLipoTrfg2RUwsg` | DNS TXT |
| 41 | dns | dns.txt | `v=spf1 ip4:171.67.219.64/27 ip4:171.67.224.0/28 ip4:171.67.43.137 ip4:171.67.43.` | DNS TXT |
| 42 | dns | dns.txt | `e2ma-verification=vnjbb` | DNS TXT |
| 43 | dns | dns.txt | `Sendinblue-code:bde1f306529e82fd2ccf9857fc09aa98` | DNS TXT |
| 44 | dns | dns.txt | `sending_domain1097582=7dcf00de01f5fc8307de59194e0a8b462cbfa2b5e32d35bfc9e5269b93` | DNS TXT |
| 45 | dns | dns.txt | `google-site-verification=n-cl_O68vbC-_UmufTZMmLLQb9wKnuUo-4FPom4m3iA` | DNS TXT |
| 46 | dns | dns.txt | `e2ma-verification=w4lgb` | DNS TXT |
| 47 | dns | dns.txt | `autodesk-domain-verification=pXMpLf7JP-86kN9Zt5jI` | DNS TXT |
| 48 | dns | dns.txt | `e2ma-verification=8uqeb` | DNS TXT |
| 49 | dns | dns.txt | `google-site-verification=C6QZVcR4K-mSTqLE_9uVC7twZdys_BRJLLVFwgGIG3E` | DNS TXT |
| 50 | dns | dns.txt | `pexip-ms-tenant-domain-verification=3f0ac106-a365-4d3b-9fb9-2a124f04d0b6` | DNS TXT |
| 51 | dns | dns.txt | `6ce2e56c0743c0db12fbb8d03c7359` | DNS TXT |
| 52 | dns | dns.txt | `google-site-verification=hIsj3ke1PYviQQm1ig-VMAlmA07GWc5vYeh2qJT56OA` | DNS TXT |
| 53 | dns | dns.txt | `bwZknJMLNV1XuaJAyUmKlAFrdZo+p5yDlTNACmDUWhgtyihfJc8oWMnK7hWLreN+ozU3mX91yHHzZx0a` | DNS TXT |
| 54 | dns | dns.txt | `e2ma-verification=a00eb` | DNS TXT |
| 55 | dns | dns.txt | `google-site-verification=1HuKdQQTxv1R8v4dxihLzji-mH23d2KchIeaxsljN6Q` | DNS TXT |
| 56 | dns | dns.txt | `adobe-idp-site-verification=4c872117a60d5c3b7d132914730b3f3e2189c67a217450a2f3bc` | DNS TXT |
| 57 | dns | dns.txt | `google-site-verification=zwyVSZ2CSXXUndqTu5itEDFvp58bOFVBPAbtrIondBU` | DNS TXT |
| 58 | dns | dns.txt | `onetrust-domain-verification=2983144927f6450ea12b5557b2080dae` | DNS TXT |
| 59 | dns | dns.txt | `e2ma-verification=n4agb` | DNS TXT |
| 60 | dns | dns.txt | `notion-domain-verification=zGjaM9fWZoGRyOnvaxST0hfeCzfxvxzJnKMTN69sYJw` | DNS TXT |
| 61 | dns | dns.txt | `00DVG000007ihZt=1TBVG0000000Ldx` | DNS TXT |
| 62 | dns | dns.txt | `atlassian-domain-verification=C9ho3V/RWWifTCqh8sF3L0PI7jVZWAL9dCxVL1gzJvr6SYJCKB` | DNS TXT |
| 63 | dns | dns.txt | `00DcX000004FChh=1TBcX00000009JR` | DNS TXT |
| 64 | dns | dns.txt | `airtable-verification=0a746053a028476f6d1671cbc9016585` | DNS TXT |
| 65 | dns | dns.txt | `htBOpqv5il135Xfa09GRiVHY09Xb9qXNj6o5lAfj8gNoBvyyGu5rSb4gvSj9lCUwY1NF0+wL2BO1ZDIc` | DNS TXT |
| 66 | dns | dns.txt | `wiz-domain-verification=2957e22f41cc73b19d44177ecf39bd1a1926a1e6362011b8f83e65aa` | DNS TXT |
| 67 | dns | dns.txt | `e2ma-verification=fq1fb-remove` | DNS TXT |
| 68 | dns | dns.txt | `airtable-verification=6deae5f718f685ac8c8c3c37418aafcf` | DNS TXT |
| 69 | dns | dns.txt | `e2ma-verification=zv1eb` | DNS TXT |
| 70 | dns | dns.txt | `pardot884873=1b7cebffc22a290049b6710c0620e741a3f4d3a720196287a95816f9afaa7695` | DNS TXT |
| 71 | dns | dns.txt | `airtable-verification=22e64691170fba22a576b309bf587b87` | DNS TXT |
| 72 | dns | dns.txt | `e2ma-verification=7x8eb` | DNS TXT |
| 73 | dns | dns.txt | `e2ma-verification=avqab` | DNS TXT |
| 74 | dns | dns.txt | `e2ma-verification=98lgb` | DNS TXT |
| 75 | dns | dns.txt | `pardot604641=4bbe27c356474886816017d9b5aea8f21f2d3c3b651096960379a441342c51fb` | DNS TXT |
| 76 | dns | dns.txt | `samsung-domain-verification=7b810e85-b3d6-4c1c-b33c-44f242e81537` | DNS TXT |
| 77 | dns | dns.txt | `airtable-verification=b8f5e3c2468d582f896b4a8f0839dd8a` | DNS TXT |
| 78 | dns | dns.txt | `e2ma-verification=m0ggb` | DNS TXT |
| 79 | dns | dns.txt | `e2ma-verification=fq1fb` | DNS TXT |
| 80 | dns | dns.txt | `e2ma-verification=5g5eb` | DNS TXT |
| 81 | dns | dns.txt | `00D46000000qFgG=1TBVH0000000Ak9` | DNS TXT |
| 82 | dns | dns.txt | `e2ma-verification=diffb` | DNS TXT |
| 83 | dns | dns.txt | `amazonses:7IodrIPH40wdjQxliaAOOqSX8rn4q7lSiSvuFZPwUnY=` | DNS TXT |
| 84 | dns | dns.txt | `e2ma-verification=dy8eb` | DNS TXT |
| 85 | dns | dns.txt | `e2ma-verification=nbxfb` | DNS TXT |
| 86 | dns | dns.txt | `airtable-verification=94cdd68161a8e41e92cc5dd7abde8eae` | DNS TXT |
| 87 | dns | dns.txt | `google-site-verification=kyvps-t3mjXwz5HBQa7oO40qvObbV8z_B1IoySwe-GY` | DNS TXT |
| 88 | dns | dns.txt | `00Dg0000006IKxz=1TBWG0000000Q49` | DNS TXT |
| 89 | dns | dns.txt | `3VCR5VZOJKXDX3AFKS202RQVEDHPD1WB04T0QNAB` | DNS TXT |
| 90 | dns | dns.txt | `remarkable-domain-verification=d359b4b2-89f8-46f3-862a-6008b632497b` | DNS TXT |
| 91 | dns | dns.txt | `e2ma-verification=cvnbb` | DNS TXT |
| 92 | dns | dns.txt | `onetrust-domain-verification=1e6b4a2989b7412499dca24f8188396b` | DNS TXT |
| 93 | dns | dns.txt | `e2ma-verification=c00eb` | DNS TXT |
| 94 | dns | dns.txt | `00DRK00000OTvMr=1TBRK0000000VIM` | DNS TXT |
| 95 | dns | dns.txt | `e2ma-verification=4x8eb` | DNS TXT |
| 96 | dns | dns.txt | `e2ma-verification=q57fb` | DNS TXT |
| 97 | dns | dns.txt | `e2ma-verification=gu1ab` | DNS TXT |
| 98 | dns | dns.txt | `e2ma-verification=7z0eb` | DNS TXT |
| 99 | dns | dns.txt | `00DVG000007pOvX=1TBVG0000000Lqr` | DNS TXT |
| 100 | dns | dns.txt | `00Dcc00000474Kj=1TBcc0000000HyX` | DNS TXT |
| 101 | dns | dns.txt | `google-site-verification=XBIgNMnjRT9eOchFldQx7rsHG9ROchX682SfSM0_1lE` | DNS TXT |
| 102 | dns | dns.txt | `e2ma-verification=b00eb` | DNS TXT |
| 103 | dns | dns.txt | `h1-domain-verification=aV4vQvSRHvQxGhvdz29L2ozsKDTReL7qKDgdjhPgzA5E7UC6` | DNS TXT |
| 104 | dns | dns.txt | `SFMC-6lLIlwvbCaTM80Tq1R1zsnKi9CqM3R6ZPPvoE6sK` | DNS TXT |
| 105 | dns | dns.txt | `e2ma-verification=07pfb` | DNS TXT |
| 106 | shodan | open_port | `80` | https://internetdb.shodan.io/171.67.215.200 |
| 107 | shodan | open_port | `443` | https://internetdb.shodan.io/171.67.215.200 |
| 108 | shodan | hostname | `www-v6.stanford.edu` | https://internetdb.shodan.io/171.67.215.200 |
| 109 | shodan | hostname | `web.stanford.edu` | https://internetdb.shodan.io/171.67.215.200 |
| 110 | shodan | hostname | `stanford.edu` | https://internetdb.shodan.io/171.67.215.200 |
| 111 | shodan | cpe | `cpe:/a:apache:http_server` | https://internetdb.shodan.io/171.67.215.200 |
| 112 | wayback | wayback.first_snapshot | `1996-12-29` | https://web.archive.org/web/19961229181022/http://www.stanford.edu:80/ |
| 113 | wayback | wayback.last_snapshot | `2003-02-13` | https://web.archive.org/web/20030213173909/http://stanford.edu:80/ |
| 114 | wayback | wayback.snapshot_count | `200` | http://web.archive.org/cdx/search/cdx |

## Trace

- plan: First run whois to capture registrar details, creation/expiry dates and name‑servers, establishing ownership and infrastructure baseline. Next query dns for A/AAAA, MX, NS, TXT and CNAME records to map hosts, mail routing and any SPF/DKIM clues. Then pull Shodan InternetDB data for those IPs to see open ports, services, hostnames and known vulnerabilities. After that search GitHub with code‑search dorks for “stanford.edu” to find accidental credential or config leaks. Finally review the Wayback Machine for historical snapshots to track changes in site structure, subdomains and exposed information over time.
- decide -> whois: Start with the cheapest tool to gather domain registration and name‑server information
- observe: whois: 0 findings (0 new), elapsed 618 ms
- decide -> dns: Gather DNS records to map hosts, mail routing, and subdomains before deeper probing
- observe: dns: 105 findings (105 new), elapsed 1126 ms
- decide -> shodan: Gather open ports, services, and host details for the IPs discovered via DNS
- observe: shodan: 6 findings (6 new), elapsed 714 ms
- decide -> github: Search GitHub for stanford.edu references to uncover possible credential or config leaks
- observe: github: 0 findings (0 new), elapsed 3024 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to gather historical snapshots of stanford.edu
- observe: wayback: 3 findings (3 new), elapsed 8372 ms
- decide -> stop: All tools have been used and evidence gathered
