#include<bits/stdc++.h>

using namespace std;

#define white 0
#define gray 1
#define black 2
vector<int>adj[1000006];
bool visited[100000]= {false};
int dis[100000]= {0},fin[100000]= {0},tim=0;
stack<int>st;
int color[100000]= {0};
bool hasCycle=false;
bool compare(int a,int b)
{
    if(a>b) return true;
    return false;
}
void dfs(int x)
{
    if(visited[x]) return;
    visited[x] = true;
    color[x]=gray;
    tim++;
    dis[x]=tim;
    for(int i=0; i<adj[x].size(); i++)
    {
        int u=adj[x][i];
        if(visited[u]&&color[u]==gray&&color[x]==gray)
        {
            hasCycle=true;
        }
        else if(!visited[u]) dfs(adj[x][i]);
    }
    color[x]=black;
    tim++;
    fin[x]=tim;
    st.push(x);
}


int main()
{
    int n,i,j,u,v,x,y,cnt=0,flag=0;
    cin>>n;
    string s[n+10];
    for(i=0; i<n; i++)
    {
        cin>>s[i];
    }
    for(i=0; i<n-1; i++)
    {
        x=s[i].size();
        y=s[i+1].size();
        cnt=0;
        for(j=0; j<min(x,y); j++)
        {

            if(s[i][j]!=s[i+1][j])
            {
                u=s[i][j];
                v=s[i+1][j];
                adj[u].push_back(v);
                cnt++;
                break;
            }

        }
        if(x>y&&cnt==0)
            flag=1;
    }
    for(i=122; i>=97; i--)
    {
        if(!visited[i])
        {
            dfs(i);

        }
    }
    if(hasCycle||flag==1)
        cout<<"Impossible"<<endl;
    else
    {
        for(i=0; i<25; i++)
        {
            x=st.top();
            printf("%c",x);
            st.pop();
        }
        x=st.top();
        printf("%c ",x);
    }
    return 0;
}
