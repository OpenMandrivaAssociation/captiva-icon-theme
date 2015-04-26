%define debug_package %{nil}
%define snap 20150427

Summary:	Captiva icon theme
Name:		captiva-icon-theme
Version:	0.0.0
Release:	2
License:	GPLv3
Group:		Graphical desktop/Other
URL:		https://github.com/captiva-project/captiva-icon-theme
# git archive --format=tar --prefix=captiva-icon-theme-0.0.0-$(date +%Y%m%d)/ HEAD | xz -vf > captiva-icon-theme-0.0.0-$(date +%Y%m%d).tar.xz
Source0:	https://github.com/captiva-project/%{name}/archive/%{name}-%{version}.tar.xz
Requires:	hicolor-icon-theme

%description
Captiva icon theme.

%prep
%setup -q

%build

%install
install -d -m 755 %{buildroot}%{_iconsdir}/Captiva
cp -afR Captiva %{buildroot}%{_iconsdir}/Captiva

%files
%doc README.md
%{_iconsdir}/Captiva
