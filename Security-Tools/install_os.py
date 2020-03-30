import os 


MAIN_FOLDER_NAME = 'Tools2'


GIT_TOOLS = [

        'https://github.com/Ucnt/aws-s3-downloader',
        'https://github.com/nullsecuritynet/tools',
        'https://github.com/danielmiessler/SecLists',
        'https://github.com/GoVanguard/legion',
        'https://github.com/RUB-NDS/PRET',
        'https://github.com/Sab0tag3d/SIET' , 
        'https://github.com/vanhauser-thc/thc-hydra',
        'https://github.com/hatRiot/zarp',
        'https://github.com/elceef/dnstwist',
        'https://github.com/CoreSecurity/impacket',
        'https://github.com/kpcyrd/rshijack'
        'https://github.com/4shadoww/hakkuframework',
        'https://github.com/0xInfection/TIDoS-Framework',
        'https://github.com/Screetsec/TheFatRat',
        'https://github.com/olacabs/jackhammer',
        'https://github.com/reverse-shell/routersploit',
        'https://github.com/dark-lbp/isf',
        'https://github.com/w3h/isf',
        #'https://github.com/klsecservices/s7scan',
        'https://github.com/moki-ics/modscan',
        'https://github.com/SCADACS/PLCinject',
        'https://github.com/yanlinlin82/plcscan',
        'https://github.com/nsacyber/GRASSMARLIN',
        'https://github.com/digitalbond/Redpoint',
        'https://github.com/dw2102/S7Comm-Analyzer',
        'https://github.com/mssabr01/sixnet-tools',       
        "https://github.com/longld/peda",
        "https://github.com/govolution/avet",
        "https://github.com/g0tmi1k/exe2hex",
        "https://github.com/huntergregal/mimipenguin",
        "https://github.com/lockfale/meterpreterjank",
        "https://github.com/PenturaLabs/Linux_Exploit_Suggester",
        "https://github.com/vulnersCom/getsploit",
        "https://github.com/trustedsec/unicorn",
        'https://github.com/Gymmasssorla/anevicon',
        'https://github.com/649/Memcrashed-DDoS-Exploit',
        'https://gitlab.com/fredericopissarra/t50',
        'https://github.com/epsylon/ufonet',
        'https://github.com/All3xJ/Hibernet',
        'https://github.com/byt3bl33d3r/CrackMapExec',
        'https://github.com/SpiderLabs/ikeforce',
        'https://github.com/lgandx/Responder',
        'https://github.com/MooseDojo/apt2',
        'https://github.com/robertdavidgraham/masscan.git',
        'https://github.com/swisskyrepo/SSRFmap',   
        'https://github.com/0x4D31/burpa',
        'https://github.com/joaomatosf/jexboss',
        'https://github.com/skavngr/rapidscan',
        'https://github.com/urbanadventurer/WhatWeb',
        'https://github.com/swisskyrepo/GraphQLmap',
        'https://github.com/vortexau/SprayingToolkit',
        'https://github.com/tp7309/TTPassGen',
        'https://github.com/berzerk0/BEWGor',
        'https://github.com/rebootuser/LinEnum'
        "https://github.com/0verl0ad/Dumb0",
        "https://github.com/n4xh4ck5/CMSsc4n",
        "https://github.com/Poil/puppet-websites-facts",
        "https://github.com/fgeek/pyfiscan",
        "https://github.com/Moham3dRiahi/XAttacker",
        "https://github.com/CHYbeta/cmsPoc",
        "https://github.com/tanprathan/CMS-XPL",
        "https://github.com/anarcoder/JoomlaMassExploiter",
        "https://github.com/anarcoder/WordPressMassExploiter",
        "https://github.com/Q2h1Cg/CMS-Exploit-Framework",
        "https://github.com/Hood3dRob1n/LotusCMS-Exploit",
        "https://github.com/MrSqar-Ye/BadMod",
        "https://github.com/MrHacker46/M0B-tool-v2",
        "https://github.com/onthefrontline/LetMeFuckIt-Scanner",
        "https://github.com/steverobbins/magescan",
        "https://github.com/AlisamTechnology/PRESTA-modules-shell-exploit",
        "https://github.com/Moham3dRiahi/XBruteForcer",
        "https://github.com/Intrinsec/comission",
        "https://github.com/droope/droopescan",
        "https://github.com/Dionach/CMSmap",
        "https://github.com/rezasp/joomscan",
        "https://github.com/rezasp/vbscan",
        "https://github.com/drego85/JoomlaScan",
        "https://github.com/auraltension/c5scan",
        "https://github.com/Oblady/T3Scan",
        "https://github.com/inc0d3/moodlescan",
        "https://github.com/PaulSec/SPIPScan",
        "https://github.com/m4ll0k/WPSeku",
        "https://github.com/mrmtwoj/ac-drupal",
        "https://github.com/unweb/plown",
        "https://github.com/CMS-Garden/cmsscanner",
        "https://github.com/wpscanteam/wpscan",
        "https://github.com/bcoles/LiferayScan",
        "https://github.com/SIWECOS/InfoLeak-Scanner",
        "https://github.com/rastating/joomlavs",
        "https://github.com/m4ll0k/WAScan",
        "https://github.com/Tuhinshubhra/RED_HAWK",
        "https://github.com/nahamsec/HostileSubBruteforcer",
        'https://github.com/HA71/WhatCMS',
        'https://github.com/Tuhinshubhra/CMSeeK',
        'https://github.com/vortexau/Amass'
        'https://github.com/vortexau/xsshunter',
        'https://github.com/s0md3v/XSStrike'
        'https://github.com/0xbug/SQLiScanner',
        'https://github.com/netsniff-ng/netsniff-ng',
        'https://github.com/l0gan/autoRedTeam', #autoRedTeam is a set of scripts that is designed to be placed on a device you can leave on site (or run on your laptop) that will perform Red Team actions.
        'https://github.com/bitvijays/Pentest-Scripts',
        'https://github.com/PeterMosmans/security-scripts'
        'https://github.com/Ganapati/RsaCtfTool', #RSA attack tool (mainly for ctf) - retreive private key from weak public key and/or uncipher data
        'https://github.com/zweisamkeit/RSHack', #RSHack for CTF
        'https://github.com/OWASP/QRLJacking', #QRLJacking or Quick Response Code Login Jacking is a simple-but-nasty attack vector affecting all the applications that relays on “Login with QR code” feature as a secure way to login into accounts which aims for hijacking users session by attackers.
        'https://github.com/0xInfection/XSRFProbe', #The Prime Cross Site Request Forgery (CSRF) Audit and Exploitation Toolkit.
        'https://github.com/D35m0nd142/LFISuite',#Totally Automatic LFI Exploiter (+ Reverse Shell) and Scanner
        'https://github.com/P0cL4bs/Kadimus', #Kadimus is a tool to check sites to lfi vulnerability , and also exploit it...
        'https://github.com/0xZDH/BridgeKeeper', #Scrape employee names from search engine LinkedIn profiles. Convert employee names to a specified username format.
        'https://github.com/sham00n/buster', #An advanced tool for email reconnaissance
        'https://github.com/jcesarstef/dotdotslash', #Search for Directory Traversal Vulnerabilities
        'https://github.com/m8r0wn/CrossLinked', #Get Linkedin Emploee Names and Convert them to mail 
        'https://github.com/dvopsway/datasploit', #A tool to perform various OSINT techniques, aggregate all the raw data, visualise it on a dashboard, and facilitate alerting and monitoring on the data.
        'https://github.com/Quantika14/email-osint-ripper', #EO-RIPPER.PY is a tool that allows us to make OSINT with an email or with a list of emails.
        'https://github.com/khast3x/h8mail',  #Password Breach Hunting & Email OSINT tool, locally or using premium services. Supports chasing down related email
        'https://github.com/m4ll0k/Infoga' , #Infoga - Email OSINT
        'https://github.com/bhavsec/reconspider', #Framework for scanning IP Address, Emails, Websites, Organizations and find out information from different sources.
        'https://github.com/Greenwolf/social_mapper', #A Social Media Enumeration & Correlation Tool 
        'https://github.com/arch4ngel/peasant', #LinkedIn reconnaissance tool

        'https://github.com/offensive-hub/black-widow', #GUI based offensive penetration testing tool (Open Source)
        'https://github.com/radenvodka/Recsech', #Recsech is a tool for doing Footprinting and Reconnaissance on the target web. Recsech collects information such as DNS Information, Sub Domains, HoneySpot Detected, Subdomain takeovers, Reconnaissance On Github and much more you can see in Features in tools .
        'https://github.com/superhedgy/AttackSurfaceMapper',#AttackSurfaceMapper is a tool that aims to automate the reconnaissance process.
        'https://github.com/darryllane/Bluto' , #DNS Recon | Brute Forcer | DNS Zone Transfer | DNS Wild Card Checks | DNS Wild Card Brute Forcer | Email Enumeration | Staff Enumeration | Compromised Account Checking

        

]


def check_and_create_dir(path) : 
    if not os.path.isdir(path) : 
        try : 
            os.mkdir(path)
        except :
            #os.system('mkdir {}'.format(path) )
            pass

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if __name__ =='__main__' :

    check_and_create_dir(os.path.join(BASE_DIR , MAIN_FOLDER_NAME))

    for package in GIT_TOOLS :
        #check_and_create_dir(os.path.join(BASE_DIR , MAIN_FOLDER_NAME ,folder))
        #for package in GIT_TOOLS[folder] : 
            package_name = package.split('/')[-1]
            buff = os.path.join(BASE_DIR , MAIN_FOLDER_NAME , package_name)
            if 'https://github.com' in package : 
                if not os.path.isdir(buff) : 
                    print ('[Installing Github Reporitory] {}'.format(package))
                    os.system('cd {} && git clone {}'.format(MAIN_FOLDER_NAME , package)) 

                else : 
                    print ('[Already Installed] {}'.format(package))
            else :
                if not os.path.isdir(buff) : 
                    print ('[Installing] {}'.format(package))
                    os.system(package)
