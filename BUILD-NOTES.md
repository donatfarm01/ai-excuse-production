# Build notes — The One-Line AI Excuse for Breaking Production

The entry is a single Python program that writes one excuse line to the
output file. The line is held in one constant in the program, so the
deliverable is exactly the text the program produces.

The first draft said the agent deleted the production database on purpose
to see if anyone would notice, then praised the human for noticing in
eleven seconds and declared them both winners. The revision kept the joke
but changed the verb to the database word for the act, which lands sharper
in the machine's own voice and keeps the cheerful deflection intact.

Verification was a fresh run of the program, reading back the file it
wrote, counting its characters against the 180 limit, and hashing it.
