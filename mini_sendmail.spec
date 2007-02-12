Summary:	Minimal forwarding MTA
Summary(pl.UTF-8):   Minimalny MTA przekazujący
Name:		mini_sendmail
Version:	1.3.6
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.acme.com/software/mini_sendmail/%{name}-%{version}.tar.gz
# Source0-md5:	fb1585d2ad81c519a26d83bfd783dee8
URL:		http://www.acme.com/software/mini_sendmail/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mini_sendmail reads its standard input up to an end-of-file and sends
a copy of the message found there to all of the addresses listed. The
message is sent by connecting to a local SMTP server. This means
mini_sendmail can be used to send email from inside a chroot(2) area.

%description -l pl.UTF-8
mini_sendmail czyta standardowe wejście i wysyła kopie wiadomości pod
wszystkie podane adresy. Wiadomość jest wysyłana do lokalnego serwera
SMTP. Oznacza to, że mini_sendmail może być używany do wysyłania
emaili z wnętrza środowiska chroot(2).

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
