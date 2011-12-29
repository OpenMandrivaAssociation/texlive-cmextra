# revision 14075
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-cmextra
Version:	20111103
Release:	1
Summary:	TeXLive cmextra package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmextra.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive cmextra package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/cmextra/cmbxcd10.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmbxti12.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmbxti7.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmcscsl10.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmfibs8.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmitt12.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmitt9.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmsl6.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmsltt9.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmssbxo10.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmsslu30.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmssu30.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmvtti10.mf
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmbxcd10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmbxti12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmbxti7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmcscsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmfibs8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmitt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmitt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmsl6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmsltt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmssbxo10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmsslu30.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmssu30.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmvtti10.tfm

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
