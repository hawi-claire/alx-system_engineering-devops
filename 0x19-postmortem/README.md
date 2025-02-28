# The case of the Vanishing Varnish: A Postmortem
<p align="center">
  <img src=images/Domino picture. ALX postmortem task.jpg />
</p>
## Issue Summary

Duration: 1 hour and 15 minutes (14:30 UTC to 15:45 UTC, October 26, 2023).
Impact: Our image processing service, "PixelPerfect," experienced a complete outage. Users attempting to upload or retrieve images received 503 Service Unavailable errors. Approximately 80% of active users were affected, leading to significant frustration and a spike in support tickets.
Root Cause: An unexpected configuration change in our Varnish caching layer resulted in all cached objects being invalidated, overwhelming our backend servers.
Timeline

14:30 UTC - Issue detected: Users began reporting image upload and retrieval failures via our support channels.
14:32 UTC - Monitoring alert triggered: Our automated monitoring system flagged a significant increase in 503 errors on the PixelPerfect service.
14:35 UTC - Initial investigation: Engineers began checking backend server logs and network connectivity. Initial assumption was a database connection issue.
14:40 UTC - Database connection tests: Database connections were verified, and no issues were found.
14:50 UTC - Misleading investigation: Engineers focused on load balancer health and network routing, suspecting a misconfiguration there.
15:10 UTC - Escalation: The incident was escalated to the caching and infrastructure team.
15:20 UTC - Varnish investigation: The caching team identified a recent configuration push to Varnish.
15:30 UTC - Configuration rollback: The problematic Varnish configuration was rolled back to the previous stable version.
15:45 UTC - Incident resolved: Service restored to normal operation.
Root Cause and Resolution

The root cause was a configuration change pushed to our Varnish caching servers. A script, intended to clear specific cache entries, inadvertently triggered a global cache purge. This invalidated all cached image data, forcing every request to hit our backend servers simultaneously. The sudden surge in traffic overwhelmed the backend, resulting in the 503 errors.

The resolution involved identifying the problematic configuration push and rolling it back to the previous stable version. This restored the cache and allowed the backend servers to recover.

Corrective and Preventative Measures

We need to improve our change management process and implement more robust testing for configuration changes, especially those affecting critical infrastructure components like caching layers. We will also improve our monitoring to detect global cache invalidations more quickly.

Tasks:

Implement code review for all infrastructure configuration changes.
Add automated testing for Varnish configuration changes, including simulated cache invalidation scenarios.
Enhance monitoring to include metrics for global cache invalidation events.
Implement a "canary" deployment system for Varnish configuration updates, rolling out changes to a small subset of users first.
Document the Varnish configuration change process more thoroughly.
Implement a circuit breaker for the backend servers, to prevent overload in case of a similar event.
Add a warning to the script that clears cache entries, to prevent accidentally clearing the entire cache.
