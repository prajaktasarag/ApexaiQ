Reasearch Day 1
Prepared by: Prajakta Rajesh Sarag 
Role: Intern 
Organization: APEXAIQ 
Date: August 2026 
Document Classification: Internal Research / Public Information 

Executive Summary 
Modern organizations operate increasingly complex technology environments consisting 
of endpoints, servers, network devices, cloud resources, applications and other digital 
assets. As these environments expand, organizations face a fundamental visibility 
problem: they need to know what assets exist, where those assets are, who owns them, 
how they are configured, whether they are vulnerable, whether they remain supported 
and whether they comply with organizational requirements. 
ApexaiQ positions itself as a SaaS-based, agentless and continuous asset-assurance 
platform designed to address this visibility and risk problem. Its public materials describe 
a platform that discovers and catalogs assets, enriches asset information with lifecycle, 
vulnerability and compliance information, assesses risk and helps organizations 
determine where action is required. [Source: ApexaiQ public product material] 
The central observation from this research is that modern IT asset management is moving 
beyond maintaining a simple inventory of devices. An effective asset-management 
capability increasingly requires context, enrichment, risk prioritization and actionable 
intelligence. 
This report examines ApexaiQ's positioning, IT Asset Management (ITAM), agentless 
architecture, cybersecurity concepts, competing approaches and key terminology 
including vulnerabilities, obsolescence, compliance, asset hygiene, crown jewels, NVD, 
patch management, MSPs, integrations, SaaS, SOAR, Zero Trust and CAASM.  
Understanding ApexaiQ 
1. What Does ApexaiQ Do and What Industry Problem Does It Solve? 
1.1 What Does ApexaiQ Do ? 
ApexaiQ is an IT asset assurance and visibility platform that helps organizations 
keep track of what is happening across their IT environment. One of the 
problems it addresses is the lack of visibility and accountability when changes 
are made to network devices such as routers and switches. 
In companies, network devices are changed regularly for maintenance, 
troubleshooting, upgrades or other IT activities. However, sometimes these 
changes are not properly documented, are not linked to an ITSM ticket, or are 
made outside the approved maintenance window. This creates a gap between 
what actually happened in the IT environment and what is recorded in the 
organization's systems. 
ApexaiQ helps solve this by monitoring network device changes and comparing 
them with ITSM records and approved policies. It can identify: 
• Changes made without a ticket 
• Changes linked to the wrong ticket 
• Changes made outside an approved time window 
• Changes where proper accountability or documentation is missing 
It can then provide information such as who made the change, what was 
changed, when it happened, and whether it followed the required process. The 
platform works in a read-only mode, meaning it observes and reports changes 
rather than making configuration changes itself. 
1.2 Industry Problem 
The main industry problem is lack of visibility and control over IT infrastructure 
changes. When a change is not properly recorded, it can make troubleshooting, 
security monitoring and audits much more difficult. 
For example, if a network change is followed by an outage, the IT team may have 
to investigate: 
• What changed? 
• Who made the change? 
• Was it authorized? 
• Was there an ITSM ticket? 
• Was it made during the approved maintenance window? 
Without proper visibility, finding these answers can take significant time. 
How ApexaiQ Helps 
The basic process can be understood as: 
Monitor → Compare → Identify Issues → Report 
ApexaiQ monitors changes, compares them with ITSM records and approved 
policies, identifies changes that do not match, and provides reports that can be 
used for investigation and audits. 
Business Impact 
This can help organizations achieve: 
• Fewer unexpected issues and outages 
• Faster root-cause analysis 
• Better accountability for IT changes 
• Improved change-management processes 
• Better compliance and audit readiness 
• Less manual investigation 
“IT leaders today face impossible demands, manage risk, reduce spend, ensure 
uptime, and still innovate. ApexaiQ was built to give you full-spectrum control 
over your IT environment, so you’re never caught off guard again.” -Lokesh 
Aggarwal, CEO  
Understanding IT Assets 
2. What is IT asset management and why companies need asset 
management software? 
2.1  What is IT Asset Management (ITAM)? 
IT Asset Management (ITAM) is the process of identifying, tracking, managing and 
monitoring an organization's IT assets throughout their lifecycle. 
IT assets can include laptops, desktops, servers, routers, switches, software, 
cloud resources and other technology systems. 
In simple terms, ITAM helps a company answer: 
What assets do we have, where are they, who is responsible for them, and what 
is their current condition? 
According to NIST, effective ITAM provides a complete view of what assets exist, 
where they are and how they are being used. It can also help identify vulnerable 
assets and improve security. 
2.2 Why Do Companies Need Asset Management Software? 
In a large organization, asset information can be spread across different systems 
and may change frequently. Managing this information manually can result in 
outdated records, missing assets, duplicate information and poor visibility. 
Asset management software helps companies maintain a more centralized and 
up-to-date view of their IT environment. 
It can help organizations: 
• Know what IT assets they have 
• Track asset ownership and location 
• Monitor asset condition and lifecycle 
• Identify vulnerable or unsupported assets 
• Improve security and risk management 
• Support compliance and audits 
• Reduce unnecessary IT costs 
• Respond faster when problems occur 
CISA also recommends maintaining an inventory of IT assets and understanding 
which assets are most important to an organization's operations and security.  
Simple Example 
Suppose a company has 1,000 laptops. 
Without proper ITAM, the company may not easily know: 
• Which laptops are still being used 
• Which ones are outdated 
• Which have security vulnerabilities 
• Who is using them 
• Which need to be replaced 
With ITAM software, this information can be brought together so the company 
can see, manage and make better decisions about its IT assets. 
3. 3-5 competitors of Apexaiq and how they are different from 
Apexa. Case studies. 
3.1  Competitors of ApexaiQ 
Competitor 
Lansweeper 
Device42 
ServiceNow 
ITAM 
Main focus 
IT/OT/cloud asset 
discovery and inventory 
IT infrastructure 
discovery, ITAM and 
dependency mapping 
Enterprise IT asset 
lifecycle + ITSM 
How it differs from ApexaiQ 
Strong focus on discovering and 
maintaining a broad asset inventory, 
including IT, OT, IoT and cloud. It also offers 
vulnerability, lifecycle and automation 
features.  
Strong focus on deep infrastructure 
discovery, dependency mapping and 
understanding relationships between 
applications, servers, networks and other 
assets. It supports both agentless and 
agent-based discovery.  
More of a broad enterprise workflow/ITSM 
platform. Its ITAM connects asset 
management with CMDB, procurement, 
contracts, workflows and other 
ServiceNow modules.  
Competitor 
Main focus 
How it differs from ApexaiQ 
ManageEngine 
AssetExplorer 
3.2 Case Studies 
Hardware/software ITAM 
and lifecycle 
management 
1. Lansweeper — University of York 
Focuses strongly on inventory, asset 
lifecycle, software licenses, contracts, 
purchasing and ITSM-related asset 
management. It supports network 
discovery of routers, switches and other 
devices.  
The University of York had around 13,000 IT devices and struggled with 
fragmented tracking, spreadsheets and limited visibility into remote/personal 
devices. Lansweeper was used to centralize asset information and support IT 
procurement, management and security. 
According to Lansweeper's published customer story, the university estimates 
that it saves approximately £300,000 annually in IT spending.  
What this shows: Lansweeper's strength is broad asset discovery and inventory 
that can support cost management, IT operations and security. 
2. Device42 — Large Regional Bank 
A large U.S. banking and mortgage organization needed to document its network 
assets for an FDIC audit following a merger. It needed information about where 
assets were located and how they were connected. 
Device42 was used for infrastructure discovery and documentation. The 
customer reported saving more than $65,000 annually on FDIC audit-related 
work.  
What this shows: Device42 is particularly strong when organizations need 
detailed infrastructure visibility, relationships and dependency information. 
3. ServiceNow — Wipro 
Wipro had approximately 600,000 IT assets managed across five disconnected 
legacy systems. This made it difficult to maintain a centralized view of asset 
inventory and lifecycle status. 
Wipro implemented ServiceNow Hardware Asset Management and consolidated 
the systems. ServiceNow reports that this helped automate 50% of manual  
tasks and that Wipro anticipates approximately $1 million in annual hardware
cost savings.  
What this shows: ServiceNow's major strength is connecting IT asset 
management with a much larger ITSM/workflow ecosystem. 
4. ManageEngine — Lenskart 
Lenskart faced difficulties with asset tracking, lifecycle management and 
maintaining accurate inventory. ManageEngine AssetExplorer was used to 
provide visibility into its IT asset inventory and help manage assets from 
procurement through disposal. 
ManageEngine reports that this provided a more streamlined and automated 
approach to asset management.  
What this shows: ManageEngine focuses strongly on practical ITAM functions 
such as inventory, lifecycle management, tracking and IT operations. 
[ Primary sources used 
• ApexaiQ official website  
• Lansweeper — IT Asset Management  
• Device42 — IT Asset Management  
• ServiceNow — IT Asset Management  
• ManageEngine — AssetExplorer ]

4. Why Is ApexaiQ an Agentless Platform? 
ApexaiQ is designed as an agentless platform, meaning it does not require a 
separate software agent to be installed on every device in the organization's IT 
environment. 
According to ApexaiQ's own product material, the platform is built to discover 
and catalog IT assets in near real time across on-premises, co-located and 
cloud environments. It gathers information from different data sources, then 
aggregates, normalizes and enriches that information to provide visibility into 
assets, vulnerabilities, obsolescence, maintenance and compliance. 
Why is this important? 
An agentless approach allows ApexaiQ to focus on getting visibility across the IT 
environment without depending on an installed agent on every asset. This is 
useful for organizations with large or mixed environments where installing and 
maintaining agents on every device can be difficult. 
ApexaiQ's newer assessment material also describes its agentless discovery as 
“No installs” and read-only, API-driven scans, designed to map assets across 
on-premises, cloud and SaaS environments. 
The basic idea can therefore be understood as: 
Different data sources → ApexaiQ → Asset discovery and enrichment → Risk 
visibility 
In simple terms 
ApexaiQ is agentless because it is designed to discover and understand an 
organization's IT assets without requiring its own software agent to be 
installed on every device. This supports broader asset visibility while reducing 
the need to deploy and maintain additional software across the environment. 

Section 2 
Study the following concepts:  
1.Apexaiq score 
Definition: 
The ApexaiQ Score is a numerical score used by ApexaiQ to measure an organization's 
overall IT infrastructure health and risk. ApexaiQ describes the score as being based on 
information such as vulnerabilities, obsolescence, maintenance and compliance. Its 
original public material describes the score on a 60–160 scale, inspired by human IQ, 
where a higher score indicates a stronger and more secure environment.  
Why is it important? 
It gives an organization a simple way to measure its current risk, set a benchmark, and 
track whether its IT environment is improving over time. ApexaiQ describes the score as 
a “provable” measure of risk reduction.  
Simple example: 
If an organization improves its patching, removes obsolete assets and fixes compliance 
gaps, its ApexaiQ Score can be used to show whether its overall technology risk has 
improved. 
Relation to ApexaiQ: 
The score brings together the information collected and enriched by ApexaiQ into one 
measurable indicator, helping IT and security teams understand where they stand and 
what needs attention

2. IT asset management 
Definition: 
IT Asset Management (ITAM) is the process of identifying, tracking, managing and 
monitoring an organization's IT assets throughout their lifecycle. IT assets can include 
laptops, servers, network devices, software and cloud resources. NIST describes ITAM 
as helping organizations maintain visibility into their assets and manage them 
effectively. 
Why is it important? 
Companies need accurate asset information to control costs, manage lifecycle, identify 
risks, improve security and support compliance. Without proper ITAM, organizations 
may have unknown, outdated or unsupported assets. 
Simple example: 
A company has 1,000 laptops. ITAM helps it know which laptops exist, who uses them, 
where they are, whether they are supported, and when they need maintenance or 
replacement.  
Relation to ApexaiQ: 
IT asset management is closely related to ApexaiQ because the platform provides 
visibility into IT assets and can enrich asset information with areas such as 
vulnerabilities, obsolescence, maintenance and compliance, helping organizations 
understand the condition and risk of their assets. 
[NIST — IT Asset Management guidance: NIST Special Publication 1800-5: IT Asset 
Management 
ApexaiQ — Official product material: ApexaiQ Product Overview]

4. Vulnerabilities 
Definition: 
A vulnerability is a weakness in a system, software, device, process, or security control 
that could be exploited or triggered by a threat.  
Why is it important? 
Vulnerabilities can create security risks if they are not identified and addressed. 
Knowing which assets are affected helps organizations decide what needs attention 
first. 
Simple example: 
A company is using an outdated version of software that has a known security 
weakness. That software is vulnerable and may need to be updated or otherwise 
protected. 
Relation to ApexaiQ: 
ApexaiQ's asset-assurance approach connects asset information with areas such as 
vulnerabilities, lifecycle and compliance, helping organizations understand the 
condition and risk associated with their assets. 
[Primary sources: 
NIST — Vulnerability Glossary: NIST Vulnerability Definition 
NIST — Vulnerability Assessment: NIST Vulnerability Assessment]

5. Obsolescence 
Obsolescence means that an IT asset, technology, hardware or software has become 
outdated and is no longer suitable or practical for current requirements. This can 
happen when newer technology replaces it or when the vendor stops supporting it. 
Why is it important? 
Obsolete technology can become harder to maintain, may not receive security updates, 
and can create operational, security and compatibility risks. 
Simple example: 
A company is still using an old network device for which the manufacturer no longer  
provides updates or support. The device may still work, but it is considered obsolete 
and may need to be replaced. 
Relation to ApexaiQ: 
ApexaiQ includes obsolescence and lifecycle information as part of its asset-assurance 
approach. This helps organizations identify assets that are becoming outdated and 
understand where lifecycle-related risk exists. 
[Primary sources: 
NIST — Glossary/IT asset management resources: NIST Computer Security Resource 
Center 
ApexaiQ — Official product material: ApexaiQ Product Overview]

5.Compliance 
Definition: 
Compliance means following the required laws, regulations, standards, policies, or 
contractual requirements that apply to an organization. 
Why is it important? 
Compliance helps organizations make sure that their systems and processes meet 
required security and operational requirements. It also provides evidence that the 
organization is following those requirements. 
Simple example: 
If a company has a policy requiring critical systems to be patched within a certain 
period, checking whether those systems meet that requirement is part of compliance. 
Relation to ApexaiQ: 
ApexaiQ's platform collects and enriches asset information with compliance data and 
provides compliance visibility and validation. Its official material describes automated 
compliance tracking and reporting, helping organizations identify gaps and improve 
their compliance posture.  
[Primary sources: 
NIST Cybersecurity Resource Center  
ApexaiQ ]

6. Maintenance 
Definition: 
IT maintenance is the process of keeping hardware, software and other IT assets 
working properly, updated and reliable throughout their lifecycle. 
Why is it important? 
Regular maintenance helps prevent failures, reduce downtime, improve security and 
extend the useful life of IT assets. It can include software updates, hardware servicing, 
configuration checks and replacing components when needed. 
Simple example: 
A company regularly updates the firmware on its network switches and replaces faulty 
hardware components to keep the network running reliably. This is part of IT 
maintenance. 
Relation to ApexaiQ: 
ApexaiQ includes maintenance information as part of its asset-assurance approach. 
This helps organizations maintain visibility into the condition and lifecycle of assets and 
identify areas where maintenance may be required. 
[Primary sources: 
• NIST — IT Asset Management: NIST Special Publication 1800-5  
• ApexaiQ — Official Product Overview: ApexaiQ Product Overview]

8. End of Life, End of Support, End of Maintenance 
These are IT asset lifecycle milestones that indicate different stages in the support of a 
product or software version. The exact meaning and dates can vary by vendor, so the 
vendor's official lifecycle policy should always be checked. Cisco, for example, defines 
separate milestones for maintenance and support, while Red Hat distinguishes End of 
Maintenance from End of Life.  
Term 
End of Life (EOL) 
End of Support 
(EOS) 
End of Maintenance 
(EOM) 
Why is it important? 
Simple meaning 
The product/version has reached the end of its lifecycle and 
is generally being discontinued or retired. 
The vendor stops providing normal technical support after 
this date. 
The vendor stops providing normal maintenance such as bug 
fixes or certain security updates. 
An asset that has reached these milestones can become harder to secure, maintain or 
troubleshoot. Organizations therefore need to identify such assets and plan upgrades or 
replacement. 
Simple example: 
A company uses an old network device. The vendor has stopped providing maintenance 
updates, and support will end later. The IT team should identify the device, assess its 
risk and plan its replacement. 
Relation to ApexaiQ: 
ApexaiQ includes lifecycle and obsolescence information as part of its asset-assurance  
approach. This helps organizations identify assets that are approaching or have passed 
important lifecycle milestones and understand the related risk. 
[Primary sources: 
• Cisco — Software lifecycle milestones:  
• Red Hat — End of Maintenance and End of Life:  
• ApexaiQ — Official product material: ApexaiQ Product Overview ]

9. Asset Hygiene 
Definition: 
Asset hygiene means keeping an organization's IT asset information accurate, 
complete, up to date and properly managed. It includes knowing what assets exist, 
their important details, ownership, status and security condition. 
Why is it important? 
Poor asset hygiene can create blind spots and security risks. CISA and NIST 
emphasize maintaining accurate, up-to-date asset inventories because organizations 
need visibility into their assets to manage cybersecurity risk effectively.  
Simple example: 
A company discovers that some network devices are missing from its inventory and 
several records contain outdated information. Cleaning these records, identifying the 
missing devices and keeping the inventory updated is part of improving asset hygiene. 
Relation to ApexaiQ: 
ApexaiQ's asset-assurance approach is relevant because it helps organizations 
discover, organize and enrich asset information, making it easier to identify issues 
such as vulnerabilities, obsolescence, maintenance and compliance gaps. 
Key takeaway: 
Good asset hygiene means having a clean, accurate and current view of your IT 
environment so that assets and their risks can be managed properly. 
[Primary sources: 
• NIST — Asset Management as a Foundation for OT Cybersecurity 
• CISA — Improving Asset Visibility and Vulnerability Detection

10. Crown Jewel 
Definition: 
A crown jewel is an asset that is especially important to an organization because its 
loss, damage, or compromise could seriously affect the business. CISA describes 
15 
critical assets as things essential to an organization's operations or mission, including 
systems, technology and important data.  
Why is it important? 
Not all IT assets have the same importance. Identifying crown jewels helps an 
organization decide which assets need the highest level of protection and attention. 
NIST recommends identifying critical assets so security resources can be prioritized 
based on business impact.  
Simple example: 
For a bank, its customer database or core banking system could be a crown jewel 
because losing access to it or compromising it could seriously affect the business. 
Relation to ApexaiQ: 
For an asset-assurance platform, identifying the most important assets provides useful 
context when evaluating vulnerabilities, compliance gaps, lifecycle issues, or other 
risks. A problem affecting a critical asset may need higher priority than the same 
problem affecting a less important asset. 
[Primary sources: 
• CISA — Insider Threat Mitigation Guide:  
• NIST — Criticality Analysis Process Model: ]

11. Inventory 
Definition: 
An IT asset inventory is a record of the technology assets an organization owns or uses, 
along with important information about those assets, such as their type, location, 
owner, software and status. NIST and CISA emphasize maintaining an accurate and up
to-date inventory as a foundation for managing IT and cybersecurity risk. 
Why is it important? 
An accurate inventory helps an organization know what assets exist and what needs to 
be managed or protected. Without it, there can be unknown, outdated or unmanaged 
assets that create operational and security risks. 
Simple example: 
A company has 500 laptops, 50 servers and 20 network switches. Its inventory records 
these assets along with information such as their owner, location, operating system and 
current status. 
Relation to ApexaiQ: 
Inventory is a basic part of ApexaiQ's asset-assurance approach. ApexaiQ's official 
material describes discovering and cataloging assets and then enriching that  
information with areas such as vulnerabilities, obsolescence, maintenance and 
compliance. 
[Primary sources: 
• NIST — IT Asset Management: NIST Special Publication 1800-5 
• CISA — Improving Asset Visibility: CISA Asset Visibility Guidance 
• ApexaiQ — Official Product Overview: ApexaiQ Product Overview]

12. NVD 
Definition: 
NVD (National Vulnerability Database) is a U.S. government database maintained by 
NIST that provides information about publicly known cybersecurity vulnerabilities. It 
includes CVE records, vulnerability details, affected products, and severity information 
such as CVSS. (NVD) 
Why is it important? 
NVD helps security and IT teams identify and understand known vulnerabilities in the 
software and products they use. Its data can support vulnerability management, risk 
assessment and remediation prioritization. (NVD) 
Simple example: 
If a company uses a particular version of software that has a known CVE, an IT team can 
check the NVD to understand the vulnerability and its severity. 
Relation to ApexaiQ: 
For an asset-assurance platform like ApexaiQ, NVD data can provide useful vulnerability 
context for discovered assets—for example, helping connect an asset's software or 
product information with known vulnerabilities. 
Key takeaway: 
NVD is an official source of vulnerability information that helps organizations identify, 
understand and prioritize known security vulnerabilities. 
[Primary source: 
NIST — National Vulnerability Database: NVD Official Website 
NIST — NVD General Information: NVD General Information] 
13. Patch Management 
Definition: 
Patch management is the process of identifying, prioritizing, obtaining, installing and 
verifying software and firmware updates across an organization's systems. NIST 
describes it as an important part of preventive maintenance and cybersecurity.   
Why is it important? 
Patches often fix security weaknesses and other software problems. Keeping systems 
patched helps reduce the chance of vulnerabilities being exploited and can prevent 
security incidents and operational disruptions.  
Simple example: 
A company discovers that 50 computers are running an outdated version of software 
with a known security vulnerability. The IT team identifies those computers, prioritizes 
the update, installs the patch, and verifies that it was applied successfully. 
Relation to ApexaiQ: 
Patch management depends on having accurate asset and vulnerability information. 
ApexaiQ's asset-assurance approach can provide visibility into assets and their 
vulnerability/lifecycle status, which helps organizations understand which assets may 
require attention. 
[Primary source: 
NIST — SP 800-40 Rev. 4: Guide to Enterprise Patch Management Planning NIST SP 800
40 Rev. 4]

14. Data Breaches 
Definition: 
A data breach occurs when information is accessed, disclosed, altered, or exposed 
without proper authorization. The information could include customer data, financial 
information, credentials, or company records. NIST defines a breach as the loss of 
control, compromise, unauthorized disclosure, unauthorized acquisition, or similar 
access to protected information. 
Why is it important? 
A data breach can result in financial loss, privacy issues, operational disruption, 
reputational damage and legal or regulatory consequences. 
Simple example: 
If an attacker gains unauthorized access to a company's customer database and copies 
customer information, it may be considered a data breach. 
Relation to ApexaiQ: 
Good asset visibility can help organizations understand where important systems and 
data-related assets are located and what security issues may affect them. Identifying 
vulnerable, outdated or poorly managed assets can help reduce the risk of incidents 
that could lead to a data breach. 
[Primary sources: 
• NIST — Breach: NIST Cybersecurity Glossary – Breach,] 
 
15. MSP 
Definition: 
A Managed Service Provider (MSP) is a company that provides ongoing IT services and 
management for other organizations. An MSP may manage services such as IT 
infrastructure, networks, applications or security on behalf of its customers. NIST notes 
that many organizations use MSPs to manage their IT infrastructure, cybersecurity and 
related operations.  
Why is it important? 
MSPs allow companies to get continuous IT support and management without having to 
manage every IT function themselves. Since an MSP may manage IT for multiple 
customers, it needs good visibility and security controls across those environments. 
Simple example: 
A small company hires an MSP to manage its servers, network devices, security 
monitoring and IT support instead of having a large internal IT team. 
Relation to ApexaiQ: 
ApexaiQ has a specific MSP multi-tenant solution, designed to allow MSPs to manage 
multiple customers from a single dashboard. Its official material highlights centralized 
asset visibility, risk management, compliance, vulnerabilities and integrations across 
customer environments. 
[Primary sources: 
• NIST — Improving Cybersecurity of Managed Service Providers: NIST MSP 
Cybersecurity Project 
• ApexaiQ — MSP Multi-Tenant Solution: ApexaiQ MSP Solution]

16. Device Types 
Definition: 
Device types refer to the different kinds of hardware and computing resources that exist 
within an organization's IT environment. Common examples include laptops, desktops, 
servers, routers, switches, firewalls, mobile devices, printers and IoT devices. 
Why is it important? 
Knowing the different types of devices helps an organization maintain an accurate 
inventory and understand what needs to be managed, secured, maintained and 
monitored. 
Simple example: 
A company may have 500 laptops, 30 servers, 20 switches and 10 firewalls. Knowing 
these device types helps the IT team understand the size and structure of its 
environment. 
Relation to ApexaiQ: 
ApexaiQ's platform is designed to provide visibility across an organization's IT 
environment and discover and catalog different assets. Identifying device types helps 
organize the inventory and provides context for assessing issues such as vulnerabilities, 
lifecycle status, maintenance and compliance. 
[Primary sources: 
• NIST — IT Asset Management: NIST Special Publication 1800-5 
• CISA — Asset Inventory Guidance: CISA Asset Visibility and Vulnerability 
Detection 
• ApexaiQ — Official Product Overview: ApexaiQ Product Overview]

17. True SaaS 
Definition: 
SaaS (Software as a Service) means software that is hosted by a provider and accessed 
by customers over a network, usually through a web browser or application. In a SaaS 
model, the provider manages the underlying infrastructure and the customer mainly 
uses and configures the software. 
Why is it important? 
SaaS reduces the need for customers to install and maintain the underlying software 
and infrastructure themselves. The provider is responsible for operating and 
maintaining the service.  
Simple example: 
Instead of installing and maintaining an asset-management application on its own 
servers, a company accesses the software online while the provider manages the 
application and infrastructure. 
Relation to ApexaiQ: 
ApexaiQ describes itself in its official material as a SaaS-based, agentless platform. 
This means customers use ApexaiQ as a hosted service rather than having to deploy the 
underlying platform themselves. 
[Primary sources: 
• NIST — Software as a Service (SaaS): NIST SaaS Glossary 
• NIST — The Definition of Cloud Computing (SP 800-145): NIST SP 800-145 
• ApexaiQ — Official Product Overview: ApexaiQ Product Overview] 

18. Inbound / Outbound Integration 
Definition: 
An integration is a connection between two systems that allows them to exchange 
information or work together. 
• Inbound integration: Data comes into ApexaiQ from another system. 
• Outbound integration: Data or information goes from ApexaiQ to another system. 
Simple example: 
A security tool sends asset information to ApexaiQ → Inbound. 
ApexaiQ sends a finding or report to an ITSM/ticketing system → Outbound. 
Why is it important? 
Organizations use many different IT and security tools. Integrations allow these systems 
to share information instead of keeping data separately, which improves visibility and 
reduces manual work. 
Relation to ApexaiQ: 
ApexaiQ's official material describes integrations with existing IT and security systems 
so that asset information can be collected, enriched and used across the environment. 
Key takeaway: 
Inbound integration brings information into ApexaiQ, while outbound integration sends 
information from ApexaiQ to other systems. Together, they help connect different IT and 
security tools. 
[Primary sources: 
• NIST — Integration / Interoperability concepts: NIST Computer Security Resource 
Center 
• ApexaiQ — Official Product Overview: ApexaiQ Product Overview]

19. Compliance Standards and Related Terms 
Definition: 
Compliance standards and frameworks are requirements or guidelines that 
organizations use to manage security, privacy and business risks. They help 
organizations define what security practices should be followed and provide a way to 
assess whether those practices are being followed. 
The terms in your list are not all compliance standards: 
• ISO/IEC 27001 — An international standard for an Information Security 
Management System (ISMS).  
• HIPAA — A U.S. law containing requirements for protecting certain health 
information. 
• CISA — The U.S. Cybersecurity and Infrastructure Security Agency; it provides 
cybersecurity guidance and resources. It is not a compliance standard. 
• CISO — Chief Information Security Officer, the person/role responsible for 
leading an organization's information-security program. It is not a standard. 
Why is it important? 
Compliance helps organizations ensure that their security practices meet applicable 
legal, regulatory, contractual or organizational requirements and helps provide 
evidence that required controls are in place. 
Simple example: 
A healthcare organization handling protected health information needs to follow 
applicable HIPAA requirements. An organization using ISO/IEC 27001 may implement 
an ISMS and undergo assessment against the standard's requirements. 
Relation to ApexaiQ: 
Compliance is relevant to ApexaiQ because its platform provides visibility into assets 
and can associate asset information with compliance requirements and gaps, helping 
organizations monitor their compliance posture. 
[Primary sources: 
• ISO — ISO/IEC 27001: ISO/IEC 27001 Information Security Management 
Systems 
• U.S. HHS — HIPAA: HIPAA for Professionals 
• CISA — Official website: Cybersecurity and Infrastructure Security Agency 
• ApexaiQ — Official Product Overview: ApexaiQ Product Overview]
 
20. Perimeter 
Definition: 
A security perimeter is the boundary that separates an organization's trusted internal 
environment from external or untrusted networks. Traditionally, this boundary was 
mainly the company's network firewall and internet connection. 
Why is it important? 
The perimeter helps control who and what can access internal systems. Protecting it 
can reduce unauthorized access and other security risks. 
Simple example: 
A company uses a firewall between its internal network and the public internet. The 
firewall controls which incoming and outgoing connections are allowed. 
Relation to ApexaiQ: 
ApexaiQ's asset-visibility approach is relevant because organizations need to know 
what devices and systems exist within and around their environment. This becomes 
especially important as companies use cloud services, remote work and other 
technologies that make the traditional network perimeter less clear. 
[Primary sources: 
• NIST — Zero Trust Architecture (SP 800-207): NIST SP 800-207 
• CISA — Zero Trust Maturity Model: CISA Zero Trust Maturity Model]

21. ROI and KPI 
ROI — Return on Investment 
Definition: 
ROI measures the financial benefit an organization receives from an investment 
compared with the cost of that investment. 
Formula: 
ROI = (Gain from Investment − Cost of Investment) / Cost of Investment × 100 
Why is it important? 
ROI helps a company decide whether a technology or solution is providing enough 
value compared with what it costs. 
Simple example: 
If a company spends ₹1 lakh on an IT management solution and saves ₹1.5 lakh 
through reduced manual work and unnecessary costs, the investment has generated 
a positive return. 
Relation to ApexaiQ: 
For ApexaiQ, ROI can be considered through benefits such as less manual 
investigation, better asset visibility, faster problem identification and reduced 
operational or compliance effort. 
KPI — Key Performance Indicator 
Definition: 
A KPI is a measurable value used to track how well an organization, process or 
system is achieving a specific objective. 
Simple example: 
An IT team may track: 
• Percentage of assets discovered 
• Number of unresolved vulnerabilities 
• Patch compliance rate 
• Mean time to resolve an issue 
Relation to ApexaiQ: 
KPIs can help organizations measure whether their IT environment is improving. For 
example, an organization could track asset coverage, vulnerability remediation or 
compliance status over time. 
[Primary sources: 
• NIST — Performance measurement and metrics: NIST Cybersecurity 
Framework 2.0 
• NIST — Cost/benefit considerations in cybersecurity: NIST Cybersecurity 
Supply Chain Risk Management Practices 
• ApexaiQ — Official Product Overview: ApexaiQ Product Overview]

22. Auto-remediation 
Definition: 
Auto-remediation means automatically taking corrective action when a security or IT 
problem is detected, instead of requiring an IT person to fix it manually. 
Why is it important? 
It can help organizations reduce manual effort, respond faster to known issues and 
maintain systems more consistently. Automation is especially useful for repetitive and 
well-defined tasks. 
Simple example: 
A system detects that a device has a required security update missing and 
automatically starts an approved process to apply the update. 
Relation to ApexaiQ: 
ApexaiQ's core value is primarily around asset visibility, assessment and identifying 
issues. Its platform material also discusses integrations and actions that can support 
workflows. It is important not to assume that ApexaiQ automatically changes every 
asset; the specific action depends on the integration and workflow being used. 
[Primary sources: 
• NIST — Security Automation and Continuous Monitoring: NIST Computer 
Security Resource Center 
• CISA — Cybersecurity Performance Goals: CISA Cybersecurity Performance 
Goals 
• ApexaiQ — Official Product Overview: ApexaiQ Product Overview] 

23. Network Protocols 
Definition: 
A network protocol is a set of rules that allows devices and systems to communicate 
and exchange data over a network. 
Why is it important? 
Protocols make communication between different devices possible and help IT teams 
connect to, monitor and manage network devices. 
Simple examples: 
• TCP/IP — Basic communication across networks 
• HTTP/HTTPS — Web communication 
• DNS — Converts domain names into IP addresses 
• SSH — Secure remote access to devices 
• SNMP — Monitoring and managing network devices 
Relation to ApexaiQ: 
Network protocols are relevant to ApexaiQ's agentless approach because network and 
infrastructure information can be obtained through existing communication methods 
rather than requiring an ApexaiQ software agent to be installed on every device. 
[Primary sources: 
• NIST — Computer Security Resource Center Glossary: NIST CSRC Glossary 
• IETF — Official Internet Standards and Protocols: Internet Engineering Task Force 
(IETF) 
• ApexaiQ — Official Product Overview: ApexaiQ Product Overview]

24. Due Diligence 
Definition: 
Due diligence is the process of carefully investigating and evaluating something before 
making an important decision. In cybersecurity, this can include checking a vendor's 
security practices, risks, controls and compliance. 
Why is it important? 
It helps organizations identify potential risks before they become problems and make 
more informed decisions. 
Simple example: 
Before a company purchases a cloud service, it checks the provider's security controls, 
data protection practices, certifications and incident history. This is part of due 
diligence. 
Relation to ApexaiQ: 
ApexaiQ can support due diligence by providing better visibility into an organization's 
assets, vulnerabilities, lifecycle status and compliance information. This gives teams 
more information when assessing the condition and risk of their IT environment. 
[Primary sources: 
• NIST — Cybersecurity Supply Chain Risk Management: NIST SP 800-161 Rev. 1 
• NIST — Cybersecurity Framework 2.0: NIST CSF 2.0]

25. SOAR — Security Orchestration, Automation and Response 
Definition: 
SOAR stands for Security Orchestration, Automation and Response. It is a set of 
technologies that helps security teams connect security tools, automate repetitive 
tasks and coordinate responses to security incidents. NIST describes security 
automation as using automated processes to support security operations and 
response. 
Why is it important? 
Security teams often receive alerts from many different tools. SOAR helps bring these 
tools together and automate routine steps, allowing teams to respond faster and reduce 
manual work. 
Simple example: 
A security tool detects a suspicious event. A SOAR platform can automatically collect 
information about the event, check other security systems, create a ticket and notify the 
security team. 
Relation to ApexaiQ: 
SOAR and ApexaiQ can complement each other. ApexaiQ can provide asset and risk 
context, while a SOAR platform can use that information as part of an automated 
security workflow or response. 
[Primary sources: 
• NIST — Security Automation: NIST CSRC Glossary 
• CISA — Cybersecurity Automation and Orchestration resources: CISA 
Cybersecurity Resources]
 
26. Role of ITAM in Zero Trust Security Models 
Definition: 
Zero Trust is a security approach based on the principle that access should not be 
trusted automatically based on a user's or device's location. NIST describes the model 
as requiring organizations to continuously verify access based on factors such as 
identity, device and other context.  
Why is it important? 
Zero Trust requires organizations to know which users, devices and resources exist and 
whether they should be trusted for a particular action. Without accurate asset 
information, it is difficult to apply Zero Trust effectively. 
Simple example: 
A company discovers an unknown laptop connected to its network. ITAM helps identify 
and track the device, while a Zero Trust approach can use that information when 
deciding whether the device should be allowed to access company resources. 
Relation to ApexaiQ: 
ITAM provides the asset visibility and context that supports Zero Trust. ApexaiQ's asset
assurance approach can help organizations understand what assets exist and identify 
issues such as vulnerabilities, outdated assets and compliance gaps. 
[Primary sources: 
• NIST — Zero Trust Architecture (SP 800-207): NIST SP 800-207 
• CISA — Zero Trust Maturity Model: CISA Zero Trust Maturity Model 
• NIST — IT Asset Management: NIST Special Publication 1800-5]

27. Cyber Asset Attack Surface Management (CAASM) 
Definition: 
CAASM stands for Cyber Asset Attack Surface Management. It is an approach that helps 
organizations get a more complete and centralized view of their cyber assets and the 
risks associated with them. It brings together information from different security and IT 
tools to improve visibility. 
Why is it important? 
Organizations often have asset information spread across many systems. CAASM helps 
identify known, unknown, unmanaged or potentially vulnerable assets, giving security 
teams a clearer view of their attack surface. 
Simple example: 
A company has laptops recorded in its ITAM system, cloud assets in its cloud platform 
and vulnerabilities in a security scanner. CAASM can bring these sources together to 
provide a more complete picture of the organization's assets and security exposure. 
Relation to ApexaiQ: 
CAASM is closely related to ApexaiQ's asset-assurance approach because ApexaiQ 
focuses on discovering, cataloging and enriching asset information with areas such as 
vulnerabilities, lifecycle and compliance. This helps organizations move from simple 
asset inventory toward a more complete understanding of asset risk. 
[Primary sources: 
• NIST — Cybersecurity Framework 2.0: NIST CSF 2.0 
• CISA — Asset Visibility Guidance: CISA Improving Asset Visibility and 
Vulnerability Detection 
• ApexaiQ — Official Product Overview: ApexaiQ Product Overview] 

THANK YOU!! 
 
