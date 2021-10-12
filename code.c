struct xxx
{
    int a;
    int b;

};
struct yyy
{
    int c;
    int d;

};
main ()
{
    struct xxx p= {5,6}, q;
    struct yyy r;
    q=p;
    r=p;
}