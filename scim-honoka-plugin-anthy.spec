%define version  0.9.0
%define release  %mkrel 2
%define src_name honoka-plugin-anthy

%define honoka_version   0.9.0
%define anthy_version    6606

Name:       scim-honoka-plugin-anthy
Summary:    An Anthy input plugin for honoka
Version:    %{version}
Release:    %{release}
Group:      System/Internationalization
License:    GPL
URL:        http://nop.net-p.org/modules/pukiwiki/index.php?%5B%5Bhonoka%5D%5D
Source0:    http://nop.net-p.org/files/honoka/%{src_name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:      anthy >= %{anthy_version}
Requires:      scim-honoka-plugin-ascii     >= %{honoka_version}
Requires:      scim-honoka-plugin-kanainput >= %{honoka_version}
Requires:      scim-honoka-plugin-romkan    >= %{honoka_version}
Requires:      scim-honoka-plugin-simpleprediction >= %{honoka_version}
BuildRequires: scim-honoka-devel >= %{honoka_version}
BuildRequires: anthy-devel >= %{anthy_version}
BuildRequires: automake
BuildRequires: libltdl-devel

%description
An Anthy input plugin for honoka.

%prep
%setup -q -n %{src_name}-%{version}

%build
autoreconf
[[ -f configure ]] || ./bootstrap

%configure2_5x
# (tv) parallel build is broken:
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove devel files
rm -f $RPM_BUILD_ROOT/%{scim_plugins_dir}/honoka/*.{a,la}

%find_lang honoka-plugin-anthy

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f honoka-plugin-anthy.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README.jp
%{scim_plugins_dir}/honoka/*.so
