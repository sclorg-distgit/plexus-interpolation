%{?scl:%scl_package plexus-interpolation}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}plexus-interpolation
Version:        1.22
Release:        7.2%{?dist}
Summary:        Plexus Interpolation API
License:        ASL 2.0 and ASL 1.1 and MIT
URL:            https://github.com/codehaus-plexus/plexus-interpolation
BuildArch:      noarch

Source0:        https://github.com/sonatype/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz#/%{pkg_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-components:pom:)

%description
Plexus interpolator is the outgrowth of multiple iterations of development
focused on providing a more modular, flexible interpolation framework for
the expression language style commonly seen in Maven, Plexus, and other
related projects.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}
%pom_remove_plugin :maven-release-plugin

%build
%mvn_file : plexus/interpolation
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1.22-7.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.22-7.1
- Automated package import and SCL-ization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.22-6
- Remove BR on maven-release-plugin

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.22-3
- Cleanup spec file

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.22-2
- Update upstream URL

* Fri Nov 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.22-1
- Update to upstream version 1.22

* Thu Oct 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.21-1
- Update to upstream version 1.21

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.15-8
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.15-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 1.15-4
- Build with xmvn

* Mon Nov 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.15-3
- Fix source URL to be stable

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Alexander Kurtakov <akurtako@redhat.com> 1.15-1
- Update to latest upstream.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 27 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.14-2
- Use add_maven_depmap macro
- Use more precise specification of files

* Tue Jul 26 2011 Jaromir Capik <jcapik@redhat.com> - 1.14-2
- Removal of plexus-maven-plugin dependency (not needed)
- Minor spec file changes according to the latest guidelines

* Tue May 17 2011 Alexander Kurtakov <akurtako@redhat.com> 1.14-1
- Update to upstream 1.14 version.
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 1.13-2
- Fix review comments.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 1.13-1
- Initial package.
