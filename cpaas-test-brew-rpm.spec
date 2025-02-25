Name:	cpaas-test-brew-rpm	
Version:	4.13.0	
Release:	1
Summary:	Most simple RPM package

Group:		
License:	FIXME
URL:  http://example.com		
Source0:	

BuildRequires:	
Requires:	

%description
Dummy RPM package
test product rpm package
take #0
Webhook check #0
webhook check #1
webhook check #2
performance test #0
performance test #1
performance test #2

%prep
%setup -q


%build
cat > hello_world.py <<EOF
#!/usr/bin/env python3

def main():

    print("Hello world!")

if __name__=="__main__":
    main()


EOF

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hello_world.py %{buildroot}/usr/bin/hello_world.py


%files
/usr/bin/hello_world.py



%changelog
#TODO
