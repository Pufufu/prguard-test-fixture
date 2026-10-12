# PRGuard test fixture

Small demonstration repository for testing PRGuard.
The test PR deliberately removes division-by-zero handling.
It is a test case, not a proposed production improvement.

Expected finding: `divide(1, 0)` raises `ZeroDivisionError` after the change.
