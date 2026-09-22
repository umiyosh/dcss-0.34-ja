-- The initial dictionary is intentionally empty. These check that the Lua
-- API shares the exact-source fallback and format contract with C++.
test.eq(crawl.jtrans("Untranslated message fixture."),
        "Untranslated message fixture.")
test.eq(crawl.jtrans(" Exact key with spaces. "),
        " Exact key with spaces. ")
test.eq(crawl.jtrans("line one\nline two"), "line one\nline two")
test.eq(crawl.jtrans("one\0two"), "one\0two")
test.eq(string.format(crawl.jtrans_format("Fixture %s: %d%%"), "x", 12),
        "Fixture x: 12%")
