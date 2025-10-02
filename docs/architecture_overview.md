\# Architecture Overview  



Three-tier idea with emphasis on the application tier:  



\*\*Presentation:\*\* minimal Flask app returning a “dashboard” message  

\*\*Logic:\*\* Flask handles requests; simulates useful work  

\*\*Data:\*\* referenced as S3 in the broader picture (not implemented here)  



\## AWS components  

\- Application Load Balancer (ALB): distributes HTTP across EC2 instances  

\- EC2 Auto Scaling group: identical app servers across multiple Availability Zones  

\- VPC + subnets: isolation and routing  

\- CloudWatch: CPU/network metrics for visibility  

\- CloudShell: traffic generation with ApacheBench  



\*\*Flow:\*\*  

Clients → ALB (HTTP 80) → EC2 Auto Scaling targets (multi-AZ) → app responds  



\### Notes  

\- Use the ALB’s DNS as the client-facing entry point  

\- Multi-AZ improves fault tolerance; refresh to see hosts/zones change  

\- Security groups are the first line of defense; lock down inbound ports  



