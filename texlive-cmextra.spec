# revision 32831
# category Package
# catalog-ctan /systems/knuth/local
# catalog-date 2012-06-11 20:26:30 +0200
# catalog-license knuth
# catalog-version undef
Name:		texlive-cmextra
Version:	20170414
Release:	1
Summary:	Knuth's local information
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/local
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmextra.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of experimental programs and developments based
on, or complementary to, the matter in his distribution
directories.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/cmextra/bible12.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmbxcd10.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmbxti12.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmbxti7.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmcscsl10.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmfibs8.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmitt12.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmitt9.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmman.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmntex10.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmntt10.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmsl6.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmsltt9.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmssbxo10.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmsslu30.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmssu30.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmsytt10.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmtim.mf
%{_texmfdistdir}/fonts/source/public/cmextra/cmvtti10.mf
%{_texmfdistdir}/fonts/source/public/cmextra/diam12.mf
%{_texmfdistdir}/fonts/source/public/cmextra/gen.mf
%{_texmfdistdir}/fonts/source/public/cmextra/gen10.mf
%{_texmfdistdir}/fonts/source/public/cmextra/gen8.mf
%{_texmfdistdir}/fonts/source/public/cmextra/gen9.mf
%{_texmfdistdir}/fonts/tfm/public/cmextra/bible12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmbxcd10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmbxti12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmbxti7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmcscsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmfibs8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmitt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmitt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmman.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmntex10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmntt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmsl6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmsltt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmssbxo10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmsslu30.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmssu30.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmsytt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmtim.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/cmvtti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/diam12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/gen10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/gen8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmextra/gen9.tfm

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
