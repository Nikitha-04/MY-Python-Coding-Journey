class Solution {
public:
    string smallestNumber(string num, long long t) {
        int n = num.size();
        long long tmp = t;
        int e2=0,e3=0,e5=0,e7=0;
        while (tmp % 2 == 0) { tmp/=2; e2++; }
        while (tmp % 3 == 0) { tmp/=3; e3++; }
        while (tmp % 5 == 0) { tmp/=5; e5++; }
        while (tmp % 7 == 0) { tmp/=7; e7++; }
        if (tmp != 1) return "-1";

        // digit -> (e2,e3,e5,e7)
        int dig[10][4] = {
            {0,0,0,0}, //0 unused
            {0,0,0,0}, //1
            {1,0,0,0}, //2
            {0,1,0,0}, //3
            {2,0,0,0}, //4
            {0,0,1,0}, //5
            {1,1,0,0}, //6
            {0,0,0,1}, //7
            {3,0,0,0}, //8
            {0,2,0,0}  //9
        };

        const int INF = INT_MAX/2;
        vector<vector<int>> minCount(e2+1, vector<int>(e3+1, INF));
        minCount[0][0] = 0;
        queue<pair<int,int>> q;
        q.push({0,0});
        int trans[6][2] = {{1,0},{0,1},{2,0},{1,1},{3,0},{0,2}};
        while(!q.empty()){
            auto pr = q.front(); q.pop();
            int a=pr.first, b=pr.second;
            int d0 = minCount[a][b];
            for (auto &tr: trans) {
                int na = min(e2, a+tr[0]);
                int nb = min(e3, b+tr[1]);
                if (minCount[na][nb] > d0+1) {
                    minCount[na][nb] = d0+1;
                    q.push({na,nb});
                }
            }
        }

        auto feasible = [&](long long rE2, long long rE3, long long rE5, long long rE7, long long slots) -> bool {
            rE2 = max(0LL, rE2);
            rE3 = max(0LL, rE3);
            rE5 = max(0LL, rE5);
            rE7 = max(0LL, rE7);
            return (long long)minCount[rE2][rE3] + rE5 + rE7 <= slots;
        };

        auto fillFn = [&](long long rE2, long long rE3, long long rE5, long long rE7, long long slots) -> string {
            string res;
            for (long long k=0;k<slots;k++){
                for (int d=1; d<=9; d++){
                    long long a=dig[d][0], b=dig[d][1], c=dig[d][2], dd=dig[d][3];
                    long long nE2 = max(0LL, rE2-a);
                    long long nE3 = max(0LL, rE3-b);
                    long long nE5 = max(0LL, rE5-c);
                    long long nE7 = max(0LL, rE7-dd);
                    if (feasible(nE2,nE3,nE5,nE7, slots-k-1)) {
                        res += char('0'+d);
                        rE2=nE2; rE3=nE3; rE5=nE5; rE7=nE7;
                        break;
                    }
                }
            }
            return res;
        };

        long long totalMin = (long long)minCount[e2][e3] + e5 + e7;

        if (num.find('0') == string::npos) {
            long long te2=0,te3=0,te5=0,te7=0;
            for (char ch: num) {
                int d = ch-'0';
                te2+=dig[d][0]; te3+=dig[d][1]; te5+=dig[d][2]; te7+=dig[d][3];
            }
            if (te2>=e2 && te3>=e3 && te5>=e5 && te7>=e7) return num;
        }

        int j0 = (int)num.find('0');
        if (j0 == (int)string::npos) j0 = n;

        vector<long long> pe2(n+1,0), pe3(n+1,0), pe5(n+1,0), pe7(n+1,0);
        for (int idx=0; idx<n; idx++){
            int d = num[idx]-'0';
            long long a=0,b=0,c=0,dd=0;
            if (d!=0){ a=dig[d][0]; b=dig[d][1]; c=dig[d][2]; dd=dig[d][3]; }
            pe2[idx+1]=pe2[idx]+a;
            pe3[idx+1]=pe3[idx]+b;
            pe5[idx+1]=pe5[idx]+c;
            pe7[idx+1]=pe7[idx]+dd;
        }

        string answer = "";
        bool found = false;
        for (int i=n-1;i>=0;i--){
            if (i > j0) continue;
            int dnum = num[i]-'0';
            for (int d=dnum+1; d<=9; d++){
                long long a=dig[d][0], b=dig[d][1], c=dig[d][2], dd=dig[d][3];
                long long te2=pe2[i]+a, te3=pe3[i]+b, te5=pe5[i]+c, te7=pe7[i]+dd;
                long long rE2=e2-te2, rE3=e3-te3, rE5=e5-te5, rE7=e7-te7;
                long long slots_after = n-1-i;
                if (feasible(rE2,rE3,rE5,rE7,slots_after)) {
                    string suffix = fillFn(rE2,rE3,rE5,rE7,slots_after);
                    answer = num.substr(0,i) + char('0'+d) + suffix;
                    found = true;
                    break;
                }
            }
            if (found) break;
        }

        if (found) return answer;

        long long L = max((long long)(n+1), totalMin);
        return fillFn(e2,e3,e5,e7,L);
    }
};
