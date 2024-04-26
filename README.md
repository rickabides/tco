### Revised Total Cost of Ownership (TCO) Report: On-Premises vs. AWS Cloud Over 3 Years

#### Introduction
This report provides an  analysis of the total cost of ownership for maintaining an on-premises infrastructure compared to building on AWS Cloud services. It incorporates specific details about the on-premises setup, including hardware specifications, network architecture, and administrative overheads. The comparison is made over a three-year period, reflecting both setups' cumulative costs.

#### Infrastructure Specification
**On-Premises Specification:**
- **Web Servers:** 4 Production, 6 Development and QA servers with 1 CPU, 6 cores, 2.6 GHz, 4 GB RAM, 400 GB HDD, running Linux Ubuntu.
- **Database Servers:** 2 Production, 2 Development and QA servers with 2 CPUs, 4 cores, 1.6 GHz, 16 GB RAM, 1 TB database on MySQL.
- **Storage:** 12 TB SAN with a cost of $6,600 per TB, inclusive of networking gear.
- **Network:** Fully redundant setup with dual ISPs (Minimum 50 Mbps primary and 5 Mbps backup).
- **Facility:** Cage in a Tier 1 Co-location facility with dual utility providers, occupying 1.5 racks.
- **Maintenance & Overheads:** 10% maintenance across hardware/software, 15% administrative overhead.

**Growth and Discount Assumptions:**
- Annual growth rate of 30%.
- An 11% discount is applied to initial costs and maintenance.
- Choose EBS volumes for all AWS instances. The storage amount in the study includes all the storage needs for individual pieces. 

#### Cost Analysis
1. **Initial Setup Costs:**
   - **On-Premises:** $147,097.80 after applying the 11% discount, covering hardware, software, and initial configuration.

2. **Annual Operating Costs (Including Maintenance and Growth):**
   - **Year 1:**
     - **On-Premises:** $164,014.05, with maintenance adjusted annually for 30% growth.
     - **AWS Cloud:** $22,165.79, including service fees for EC2, RDS, and EBS.
   - **Year 2:**
     - **On-Premises:** $186,005.17, reflecting increased usage and maintenance costs.
     - **AWS Cloud:** $28,815.53, scaling up services as needed.
   - **Year 3:**
     - **On-Premises:** $214,593.63, further increasing due to growth and maintenance.
     - **AWS Cloud:** $37,460.19, adjusted for continued service scaling.

3. **Cumulative Costs Over 3 Years:**
   - **On-Premises:** $564,593.63 (sum of yearly costs plus initial setup).
   - **AWS Cloud:** $88,441.51 (annual AWS costs accumulated over three years).

#### Conclusion
The specifications of the on-premises infrastructure highlights the significant upfront and ongoing costs associated with maintaining and scaling physical hardware. In contrast, AWS Cloud offers a substantially lower cost of ownership by eliminating many of these expenses and providing a flexible environment that can dynamically adapt to changing business needs. 

Storage costs present the most significant savings in this study. Providing a Storage-Area-Network (SAN) and data redundancy on-premises is a substantial upfront investment in networking and storage hardware. In contrast, in the cloud, redundancy is provided and cost is based on usage. Perhaps more importantly, the cloud gives us the ability to choose among performance tiers to match our needs. Here we consolidated all the cloud storage needs into a single performance tier for simplicity; further storage savings could be realized through right-sizing elastic block storage tiers with the workload's needs.

If we only consider cost, the benefits and operational flexibility of building in AWS or other Cloud services are recommended for scaling the proposed system. The cloud system can grow more rapidly and not require similar administrative overhead growth. This does not mean their is no room for on-premise infrastructure. Depending on the security risk tollerance and other possible business needs, connecting on-prem and cloud information systems to form hybrid clouds are also feasible designs.

#### References
[Vantage AWS Pricing API](instances.vantage.sh)
[Storage Pricing Info](https://storagepricing.org)

