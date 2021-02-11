public int strStr(String haystack, String needle) {
    if (needle == null || needle.length() == 0)
        return 0;
    if (haystack == null || haystack.length() == 0 || needle.length() > haystack.length())
        return -1;

   char[] string = haystack.toCharArray(), pattern = needle.toCharArray();

// 创建 next 数组，next[i] 表示当前已匹配串 [0, i] 中最大相同前后缀中的前缀结尾下标。
int[] next = new int[pattern.length];
// [0, 0] 长度的字符串，就一个字符，没有任何前后缀概念，因此为 -1。
next[0] = -1;
int i = 1;// 当前要初始化的元素，即我们要找 0 到 i 字符串（称作 si）的相同前后缀，因为第 0 个字符已经初始化了，从 1 开始。

int k = -1;// 0 到 i - 1 字符串（称作 si_1)) 的相同前后缀中的前缀（称作 si_1_pre）的结尾下标，如果 si_1 没有相同前后缀，则等于 0。

while (i < next.length) {
    // si_1 存在相同前后缀
    if (k != -1) {
        /*
          * 由于 si_1 存在相同前后缀 si_1_pre 和 si_1_suf，si_1_pre 固定在字符串首部，当前字符接在 si_1_suf 后面。
          * 所以如果 si_1_pre 的下一个字符和 si_1_suf（即当前字符）相同的话，
          si 就具有相同前后缀了。
          */
        if (pattern[i] == pattern[k + 1]) {
            next[i] = k + 1;
            k++;
            i++;
        } else {
            /*
              * 回溯：
              * 如果 si_1_pre 的下一个字符与当前字符不一致，那就 si_1_pre 就不能作为 s1 相同前后缀的一部分。
              * 不过，如果 si_1_pre（现在称作 s2）也存在相同前后缀 s2_pre 和 s2_suf 的话，
              * 由于相同， si_1_suf（现在称作 s3）也存在相同前后缀 s3_pre 和 s3_suf。
              * 所以 s2_pre == s2_suf == s3_pre == s3_suf。
              * s2_pre 在字符串首部，而 s3_suf 又在当前字符前面。因此 s2_pre 有可能可以作为 si 的相同前后缀的一部分的。
              * 所以 k 不必直接变 -1，可以回溯到 si_1_pre 的相同前后缀去。
              */
            k = next[k];
        }
    } else {
        // si_1 不存在相同前后缀，si 肯定没法利用 si_1 了，不过还是可以利用字符串第一个字符，因为有可能第一个字符和当前字符一致
        k = next[i] = pattern[0] == pattern[i] ? 0 : -1;
        i++;
    }
}
    for (int s = 0, p = 0; s < string.length; s++) {
        if (pattern[p] != string[s]) {
            // 如果主串和模式串当前字符不匹配，并且存在已匹配模式串一部分 [0, p-1]
            if (p - 1 != -1) {
                // 模式串指针退回已匹配串的前缀结尾索引的下一索引
                p = next[p - 1] + 1;
                s--;// 和 s++ 抵消, 看看p新的位置是否匹配
            }
        } else {
            p++;// 如果主串和模式串当前字符匹配，并且模式串匹配完成，返回结果
            if (p == pattern.length)
                return s - p + 1;
        }
    }
    return -1;
}
    //KMP algrithm 利用已经部分匹配这个有效信息，保持i指针不回溯，通过修改j指针，让模式串尽量地移动到有效的位置。”
//所以，整个KMP的重点就在于当某一个字符与主串不匹配时，我们应该知道j指针要移动到哪？
//当匹配失败时，j要移动的下一个位置k。存在着这样的性质：最前面的k个字符和j之前的最后k个字符是一样的。