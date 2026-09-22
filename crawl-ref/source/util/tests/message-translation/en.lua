-- The same Japanese dictionary is present, but must not affect English.
test.eq(crawl.jtrans("You blink."), "You blink.")
test.eq(crawl.jtrans("Case Key"), "Case Key")
test.eq(crawl.jtrans("case key"), "case key")
test.eq(crawl.jtrans(" Exact key with spaces. "), " Exact key with spaces. ")
test.eq(crawl.jtrans("line one\nline two"), "line one\nline two")
test.eq(crawl.jtrans("one\0two"), "one\0two")
test.eq(string.format(crawl.jtrans_format("Fixture %s: %d%%"), "x", 12),
        "Fixture x: 12%")
crawl.clear_message_store()
crawl.mpr(crawl.jtrans("You blink."))
crawl.flush_prev_message()
assert(string.find(crawl.messages(1), "You blink.", 1, true))
crawl.stderr("message-translation fixture passed: en")
