#include "catch_amalgamated.hpp"

#include "message-translation.h"

TEST_CASE("message keys preserve exact source text", "[message-translation]")
{
    CHECK(message_translation::encode_key("You blink.") == "You blink.");
    CHECK(message_translation::encode_key(" you Blink. ") == " you Blink. ");
    CHECK(message_translation::encode_key("a\\b\nc\r\td")
          == "a\\\\b\\nc\\r\\td");
}

TEST_CASE("translated printf formats preserve the argument contract",
          "[message-translation]")
{
    using message_translation::valid_format;
    CHECK(valid_format("You blink.", "瞬間移動した。"));
    CHECK(valid_format("%s hits %d times.", "%sは%d回命中した。"));
    CHECK(valid_format("%*.*f%%", "値：%*.*f%%"));
    CHECK(valid_format("%zu %lld %p", "%zu個 %lld点 %p"));
    CHECK_FALSE(valid_format("%s %d", "%d %s"));
    CHECK_FALSE(valid_format("%s", "%s %s"));
    CHECK_FALSE(valid_format("%d", "%s"));
    CHECK_FALSE(valid_format("%ld", "%d"));
    CHECK_FALSE(valid_format("%08d", "%d"));
    CHECK_FALSE(valid_format("%*s", "%s"));
    CHECK_FALSE(valid_format("%s", "%1$s"));
    CHECK_FALSE(valid_format("%s", "%n"));
    CHECK_FALSE(valid_format("%n", "%n"));
    CHECK_FALSE(valid_format("%q", "%q"));
    CHECK_FALSE(valid_format("%", "%"));
    CHECK_FALSE(valid_format("%%", "%"));
    CHECK_FALSE(valid_format("%s", "%s%"));
}

TEST_CASE("message lookup falls back safely", "[message-translation]")
{
    using message_translation::select;
    CHECK(select("You blink.", "瞬間移動した。", "ja", false)
          == "瞬間移動した。");
    CHECK(select("You blink.", "", "ja", false) == "You blink.");
    CHECK(select("You blink.", "瞬間移動した。", "en", false)
          == "You blink.");
    CHECK(select("You blink.", "瞬間移動した。", nullptr, false)
          == "You blink.");
    CHECK(select("%s hits.", "%sが命中した。", "ja", true)
          == "%sが命中した。");
    CHECK(select("%s hits.", "%dが命中した。", "ja", true) == "%s hits.");
    CHECK(select("Progress", "50%完了", "ja", false) == "50%完了");
    CHECK(select("Progress", "50%完了", "ja", true) == "Progress");
}
