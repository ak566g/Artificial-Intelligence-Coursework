#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007

bool isvalid(string s){
    if(s.size() == 0)
    return false;
    for(int i=0;i<s.size();i++){
        if(!isalpha(s[i])){
            return false;
        }
    }
    return true;
}

int howMany(string str){
    string s = "";
    for(int i=0;i<str.size();i++){
        if(str[i]!='-')s+=str[i];
    }
    vector<string>word;
    string cur="";

    for(int i=0;i<s.size();i++){
        if(s[i] == '.' || s[i] =='?' || s[i] == ',' || s[i] == '!' || s[i] == ' '){
            word.push_back(cur);
            cur="";
        }else{
            cur+=s[i];
        }
    }

    word.push_back(cur);


    int wordCount = 0;
    for(int i=0;i<word.size();i++){
        if(isvalid(word[i])){
            wordCount++;
        }
    }
    
    return wordCount;
}

int main() {
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);
    // cout.tie(NULL);
    // // string s = "he is a good programmer, he won 865 competitions, but sometimes he dont. What do you think? All test-cases should pass. Done-done?";
    // // string s = "jds dsaf lkdf kdsa fkldsf, adsbf ldka ads? asd bfdal ds bf[l. akf dhj ds 878  dwa we de 7575  dsfh ds RAMU 748 dj.";
    // string s = "b? Dl )B 4(V! A. Mk, ytg ](f 1m )cnxunur {pg?";
    // cout<<howMany(s);

    int a = 23;
    int *b = &a;
    char *c = b;
}