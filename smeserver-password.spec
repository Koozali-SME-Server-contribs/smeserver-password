# $Id: smeserver-password.spec,v 1.6 2024/09/06 01:35:36 terryfage Exp $
# Authority: dungog
# Name: Stephen Noble

%define name smeserver-password
%define version 1.3.0
%define release 4

Summary: SME Server password panel
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
Group: Networking/Daemons
Source: %{name}-%{version}.tar.xz

BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
BuildRequires: smeserver-devtools
Requires: smeserver-formmagick >= 1.4.0-12

%description
Smeserver addon panel to change password strength and password ageing

%changelog
* Thu Jul 02 2026 Brian Read <brianr@koozali.org> 1.3.0-4.sme
- Comment out lexicon validation code in spec file as no more SM1 [SME: 13357]

* Thu Jul 02 2026 Jean-Philippe Pialasse <jpp@koozali.org> 1.3.0-3.sme
- remove sm1 panel and translations [SME: 13357]
- move olde translations to sm2

* Wed Jul 01 2026 Jean-Philippe Pialasse <jpp@koozali.org> 1.3.0-2.sme
- prevent inactive acocutn from beeing locked [SME: 6778]
- utf8 fixups
- translation improvement

* Mon Jun 29 2026 Brian Read <brianr@koozali.org> 1.3.0-1.sme
- Add in SM2 panel [SME: 13357]

* Mon Oct 27 2025 Vasarhelyi Zsolt <zsoltv@koozali.org> 1.2.0-18.sme
- remove use_authtok from pam config when ldap auth is enabled [SME: 13254]

* Sun Sep 08 2024 fix-e-smith-pkg.sh by Trevor Batley <trevor@batley.id.au> 1.2.0-17.sme
- Fix e-smith references in smeserver-password [SME: 12732]

* Sat Sep 07 2024 cvs2git.sh aka Brian Read <brianr@koozali.org> 1.2.0-16.sme
- Roll up patches and move to git repo [SME: 12338]

* Sat Sep 07 2024 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.

* Fri Sep 06 2024 Terry Fage <terry.fage@gmail.com> 1.2.0-15.sme
- apply locale 2024-09-06.patch

* Wed Nov 23 2022  bunkobugsy <vasarhelyizsolt@hotmail.com> 1.2.0-14.sme
- add password history [SME: 10874]

* Mon Aug 23 2021 Terry Fage <terry.fage@gmail.com> 1.2.0-13.sme
- apply locale 2021-08-23 patch

* Wed Mar 24 2021 Brian Read <brianr@bjsystems.co.uk> 1.2.0-12.sme
- Add Update event to createlinks [SME: 11034]

* Wed Mar 24 2021 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.
  Mon May 07 2008 --> Mon May 05 2008 or Wed May 07 2008 or Mon May 12 2008 or ....
  Thu May 21 2008 --> Thu May 15 2008 or Wed May 21 2008 or Thu May 22 2008 or ....

* Tue Oct 13 2020 Brian Read <brianr@bjsystems.co.uk> 1.2.0-11.sme
- Initial import to SME10 tree [SME: 11034]

* Wed Mar 09 2016 JP Pialasse <tests@pialasse.com> 1.2.0-10.sme
- apply locale 2016-03-09 patch

* Wed Jul 1 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.0-9
- add smeserver-password-1.2.0-locale-2015-07-01.patch [SME: 8968]

* Tue Feb 10 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.0-7
- Fix the expire field error [SME: 8823]
- code done by Stefano Zamboni <zamboni@mind-at-work.it>

* Fri Feb 06 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.0-6
- Add Update event to createlinks password aging [SME: 8823]

* Sun Jun 08 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.0-2
- Initial release to contribs9
- Added locale smeserver-password-1.0.0-locale-2014-06-08.patch

* Wed Jun 04 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.0-1
- Initial release to sme9

* Sun Jul 14 2013 JP Pialasse <tests@pialasse.com> 1.0.0-32.sme
- apply locale 2013-07-14 patch
- also fix for some languages [SME: 4920]

* Sat Jun 22 2013 JP Pialasse <tests@pialasse.com> 1.0.0-31.sme
- workaround for fixing  [SME: 5915]

* Thu Jun 20 2013 JP Pialasse <tests@pialasse.com> 1.0.0-30.sme
- Add Update event to createlinks english translation of panel [SME: 4920]
- Add Update event to createlinks Error saving password properties [SME: 7038]
- Add Update event to createlinks deselecting a user and saving has not effect [SME: 5915]
- porting to sme8 

* Sun Mar 06 2011 SME Translation Server <translations@contribs.org> 1.0.0-27.sme
- apply locale 2011-03-06 patch

* Tue Mar 02 2010 SME Translation Server <translations@contribs.org> 1.0.0-26.sme
- apply locale 2010-03-02 patch

* Wed Oct 21 2009 SME Translation Server <translations@contribs.org> 1.0.0-25.sme
- apply locale 2009-10-21 patch

* Mon Aug 24 2009 SME Translation Server <translations@contribs.org> 1.0.0-24.sme
- apply locale 2009-08-24 patch

* Wed May 20 2009 SME Translation Server <translations@contribs.org> 1.0.0-23.sme
- apply locale 2009-05-20 patch

* Mon Apr 27 2009 SME Translation Server <translations@contribs.org> 1.0.0-22.sme
- apply locale 2009-04-27 patch

* Sun Mar  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-21
- Apply  1 Mar 2009 locale patch [SME: 5018]

* Thu Jan  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-20
- Apply  1 Jan 2009 locale patch [SME: 4900]

* Wed Nov  5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-19
- Apply  5 Nov 2008 locale patch

* Tue Oct 14 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-18
- Apply 14 Oct 2008 locale patch

* Sun Sep 28 2008 Stephen Noble <support@dungog.net> - 1.0.0-17
- Apply locale patch

* Tue Jul 1 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-16
- Apply 1 July 2008 locale patch

* Fri May 30 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-15
- Apply 30 May 2008 locale patch

* Sat May 24 2008 Stephen Noble <support@dungog.net> - 1.0.0-14
- rewrite user-passwd-expiration [SME 4361]

* Wed May 21 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-13
  Thu May 21 2008 --> Thu May 15 2008 or Wed May 21 2008 or Thu May 22 2008 or ....
- Apply 21 May 2008 locale patch
- Fixing changelog version entries

* Wed May 07 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-12
  Mon May 07 2008 --> Mon May 05 2008 or Wed May 07 2008 or Mon May 12 2008 or ....
- Apply 7 May 2008 locale patch
- Removed missing patch of 5 May 2008, seems not committed and is 
  superseeded by the one from 7 May 2008

* Mon May 5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-11
- Apply 5 May 2008 locale patch

* Sat Apr 26 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-10
- Add common <base> tags to e-smith-formmagick's general

* Tue Apr 22 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-9
- Added 22 April 2008 locale patch
- Moved db defaults out of spec file

* Tue Apr 1 2008 Shad L. Lords <slords@mail.com> 1.0.0-8
- Update to UTF-8 translations

* Tue Mar 11 2008 Stephen Noble <support@dungog.net> - 1.0.0-7
- update locale 2008-03-11

* Sat Mar 01 2008 Stephen Noble <support@dungog.net> - 1.0.0-6
- build on smecontribs
- default password aging = no

* Sat Mar 01 2008 Stephen Noble <support@dungog.net> - 1.0.0-5
- removed Italian lexicon for now
- removed <trans> values in general
- moved from collaboration to security

* Wed Jun 20 2007 Blaz <gxs@sishell.net>,Stefano Zamboni <zamboni@mind-at-work.it>
- 1.0.0-04
- Added functions to lock account and reset password age

* Wed Jan 24 2007 Blaz <gxs@sishell.net>
- 1.0.0-03
- Cosmetics fixes
- English typos fixing

* Wed Jan 24 2007 Stefano Zamboni <zamboni@mind-at-work.it>
- 1.0.0-02
- completed english translation

* Fri Jan 12 2007 Stefano Zamboni <zamboni@mind-at-work.it>
- 1.0.0-01
- Original version

%prep
%setup

%build
#LEXICONS=$(find root/etc/e-smith/locale/ -type f )

#for lexicon in $LEXICONS
#do
#    /sbin/e-smith/validate-lexicon $lexicon
#done

perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
%clean
rm -rf $RPM_BUILD_ROOT
%post
true
%postun
true
%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
