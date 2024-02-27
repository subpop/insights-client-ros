Name:           insights-client-ros
Version:        1
Release:        1%{?dist}
Summary:        Red Hat Insights ROS collector
License:        GPLv2+

Source0:        insights-client-ros.service
Source1:        insights-client-ros.timer
Source2:        manifest-ros.yaml
Source3:        80-insights-client-ros.preset

BuildArch:      noarch

BuildRequires: systemd-rpm-macros
Requires:       insights-client

Requires:       neofetch

%description
Sends insightful ROS information to Red Hat for automated analysis

%install
install -d %{buildroot}%{_unitdir}
install -m644 %{SOURCE0} %{buildroot}%{_unitdir}/
install -m644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -d %{buildroot}%{_presetdir}
install -m644 %{SOURCE3} -t %{buildroot}%{_presetdir}/

install -d %{buildroot}/%{_sysconfdir}/insights-client/apps
install -m644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/insights-client/apps

%post
%systemd_post insights-client-ros.service
%systemd_post insights-client-ros.timer

%postun
%systemd_postun insights-client-ros.service
%systemd_postun insights-client-ros.timer


%files
%{_unitdir}/*
%{_sysconfdir}/insights-client/apps/manifest-ros.yaml
%{_presetdir}/*

%changelog
* Tue Feb 27 2024 Link Dupont <link@redhat.com> - 1-1
- Initial package
