Summary:	Minimal forwarding MTA
Summary(pl):	Minimalny MTA przekazuj±cy
Name:		mini_sendmail
Version:	1.3.5
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.acme.com/software/mini_sendmail/%{name}-%{version}.tar.gz
# Source0-md5:	fff344184e98cff0ea4d817da9d29383
URL:		http://www.acme.com/software/mini_sendmail/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mini_sendmail reads its standard input up to an end-of-file and sends
a copy of the message found there to all of the addresses listed. The
message is sent by connecting to a local SMTP server. This means
mini_sendmail can be used to send email from inside a chroot(2) area.

%description -l pl
mini_sendmail czyta standardowe wej¶cie i wysy³a kopie wiadomo¶ci pod
wszystkie podane adresy. Wiadomo¶æ jest wysy³ana do lokalnego serwera
SMTP. Oznacza to, ¿e mini_sendmail mo¿e byæ u¿ywany do wysy³ania
emaili z wnêtrza ¶rodowiska chroot(2).

%prep
%setup -q

%build
%{__make} \
	LDFLAGS=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}
install mini_sendmail $RPM_BUILD_ROOT%{_bindir}
install mini_sendmail.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
