%define name libdiscid
%define version 0.2.2
%define release %mkrel 6
%define major 0
%define libname %mklibname discid %major
%define develname %mklibname -d discid

Summary:A Library for creating MusicBrainz DiscIDs
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://users.musicbrainz.org/~matt/%{name}-%{version}.tar.gz
License: LGPLv2+
Group: System/Libraries
Url: http://musicbrainz.org/doc/libdiscid
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libdiscid is a library for creating MusicBrainz DiscIDs from audio CDs.
It reads a CD's table of contents (TOC) and generates an identifier which
can be used to lookup the CD at MusicBrainz (http://musicbrainz.org).
Additionally, it provides a submission URL for adding the DiscID to the
database.

%package -n %libname
Summary:A Library for creating MusicBrainz DiscIDs
Group: System/Libraries
# gw for python-musicbrainz2 to depend on
Provides: %name = %version-%release

%description -n %libname
libdiscid is a library for creating MusicBrainz DiscIDs from audio CDs.
It reads a CD's table of contents (TOC) and generates an identifier which
can be used to lookup the CD at MusicBrainz (http://musicbrainz.org).
Additionally, it provides a submission URL for adding the DiscID to the
database.

%package -n %develname
Summary:A Library for creating MusicBrainz DiscIDs
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
Obsoletes: %mklibname -d discid 0

%description -n %develname
libdiscid is a library for creating MusicBrainz DiscIDs from audio CDs.
It reads a CD's table of contents (TOC) and generates an identifier which
can be used to lookup the CD at MusicBrainz (http://musicbrainz.org).
Additionally, it provides a submission URL for adding the DiscID to the
database.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%doc README AUTHORS
%_libdir/libdiscid.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/libdiscid.so
%_libdir/libdiscid.*a
%_includedir/*
%_libdir/pkgconfig/*.pc




%changelog
* Wed Feb 22 2012 abf
- The release updated by ABF

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-5mdv2011.0
+ Revision: 660234
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-4mdv2011.0
+ Revision: 602537
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-3mdv2010.1
+ Revision: 520764
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.2.2-2mdv2010.0
+ Revision: 425528
- rebuild

* Thu Oct 16 2008 Götz Waschk <waschk@mandriva.org> 0.2.2-1mdv2009.1
+ Revision: 294296
- new version
- update license
- new major

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.2.1-2mdv2009.0
+ Revision: 267812
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 25 2008 Götz Waschk <waschk@mandriva.org> 0.2.1-1mdv2009.0
+ Revision: 211239
- new version
- new major

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1.1-1mdv2008.1
+ Revision: 136550
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 Götz Waschk <waschk@mandriva.org> 0.1.1-1mdv2008.0
+ Revision: 79927
- new version
- new devel name


* Sat Nov 25 2006 Götz Waschk <waschk@mandriva.org> 0.1.0-1mdv2007.0
+ Revision: 87240
- fix provides
- Import libdiscid

* Sat Nov 25 2006 G�tz Waschk <waschk@mandriva.org> 0.1.0-1mdv2007.1
- initial package

