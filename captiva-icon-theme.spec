%define debug_package %{nil}
%define snap 20150427

Summary:	Captiva icon theme
Name:		captiva-icon-theme
Version:	0.0.0
Release:	3
License:	GPLv3
Group:		Graphical desktop/Other
URL:		https://github.com/captiva-project/captiva-icon-theme
# git archive --format=tar --prefix=captiva-icon-theme-0.0.0-$(date +%Y%m%d)/ HEAD | xz -vf > captiva-icon-theme-0.0.0-$(date +%Y%m%d).tar.xz
Source0:	https://github.com/captiva-project/%{name}/archive/%{name}-%{version}-%{snap}.tar.xz
Requires:	hicolor-icon-theme

%description
Captiva icon theme.

%prep
%setup -qn %{name}-%{version}-%{snap}

%build

%install
install -d -m 755 %{buildroot}%{_iconsdir}/Captiva
cp -afR Captiva %{buildroot}%{_iconsdir}/Captiva

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %{buildroot}%{_var}/lib/rpm/filetriggers
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-captiva.filter << EOF
^./usr/share/icons/Captiva/
EOF

cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-captiva.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/Captiva/
fi
EOF
chmod 755 %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-captiva.script

%files
%doc README.md
%{_iconsdir}/Captiva
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-captiva.*
