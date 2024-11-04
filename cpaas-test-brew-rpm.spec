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

%prep
%setup -q


%build
cat > hello-world.sh <<EOF
#!/usr/bin/bash
echo Hello world
EOF

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hello-world.sh %{buildroot}/usr/bin/hello-world.sh


%files
/usr/bin/hello-world.sh



%changelog
#TODO
