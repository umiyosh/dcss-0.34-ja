/**
 * @file
 * @brief Pure helpers for exact, format-safe message translation.
 **/

#pragma once

#include <string>
#include <vector>

namespace message_translation
{
// TextDB keys occupy one physical line. Escape backslashes first so an
// actual newline remains distinct from the two literal characters "\\n".
inline std::string encode_key(const std::string &source)
{
    std::string result;
    for (const char ch : source)
    {
        switch (ch)
        {
        case '\\': result += "\\\\"; break;
        case '\n': result += "\\n"; break;
        case '\r': result += "\\r"; break;
        case '\t': result += "\\t"; break;
        default: result += ch; break;
        }
    }
    // Avoid TextDB's comment, delimiter and cache metadata namespaces.
    if (result.compare(0, 1, "#") == 0 || result.compare(0, 4, "%%%%") == 0
        || result == "TIMESTAMP")
    {
        result.insert(0, "\\");
    }
    return result;
}

inline bool format_tokens(const std::string &text,
                          std::vector<std::string> &tokens)
{
    for (size_t pos = 0; pos < text.size(); ++pos)
    {
        if (text[pos] != '%')
            continue;
        const size_t start = pos++;
        if (pos < text.size() && text[pos] == '%')
        {
            tokens.push_back("%%");
            continue;
        }
        while (pos < text.size()
               && std::string("-+ #0").find(text[pos]) != std::string::npos)
        {
            ++pos;
        }
        if (pos < text.size() && text[pos] == '*')
            ++pos;
        else
        {
            while (pos < text.size() && text[pos] >= '0' && text[pos] <= '9')
                ++pos;
        }
        if (pos < text.size() && text[pos] == '.')
        {
            ++pos;
            if (pos < text.size() && text[pos] == '*')
                ++pos;
            else
            {
                while (pos < text.size()
                       && text[pos] >= '0' && text[pos] <= '9')
                {
                    ++pos;
                }
            }
        }
        if (pos < text.size()
            && std::string("hljztL").find(text[pos]) != std::string::npos)
        {
            const char length = text[pos++];
            if (pos < text.size() && text[pos] == length
                && (length == 'h' || length == 'l'))
            {
                ++pos;
            }
        }
        // No positional arguments or %n: translated text must not change
        // argument consumption, write to memory, or introduce a new format.
        if (pos == text.size()
            || std::string("diouxXfFeEgGaAcsp").find(text[pos])
               == std::string::npos)
        {
            return false;
        }
        tokens.push_back(text.substr(start, pos - start + 1));
    }
    return true;
}

inline bool valid_format(const std::string &source,
                         const std::string &translation)
{
    std::vector<std::string> source_tokens;
    std::vector<std::string> translated_tokens;
    return format_tokens(source, source_tokens)
           && format_tokens(translation, translated_tokens)
           && source_tokens == translated_tokens;
}

inline std::string select(const std::string &source,
                          const std::string &translation,
                          const char *language, bool formatted)
{
    if (!language || std::string(language) != "ja" || translation.empty()
        || (formatted && !valid_format(source, translation)))
    {
        return source;
    }
    return translation;
}
}
