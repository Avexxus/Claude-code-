# claude.ai account export
Drop the export's `conversations.json` here (or the whole zip). Then run:
`python3 -I scripts/extract_export.py sources/account_export/conversations.json`
That writes `patrick_lines/`: Patrick's own turns per chat, with AI context collapsed and labelled "AI, NOT PATRICK". A miner agent then sorts them into world ideas, taste notes and rulings, which feed `world/` and `foundry/PATRICK_TASTE.md`. Nothing here is canon until banked.
Only saga-related chats are copied here (19 of 158); personal chats were left out on purpose.
