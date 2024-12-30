from re import finditer, MULTILINE
from execjs import compile
import os
from datetime import datetime

execJs = '''
        function a(e, t) {
            var n = r();
            return a = function(t, i) {
                var o = n[t -= 284];
                if (void 0 === a['khmYwP']) {
                    a['ZGUIrU'] = function(e) {
                        for (var t, n, i = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=', o = '', a = '', r = 0, s = 0; n = e['charAt'](s++); ~n && (t = r % 4 ? 64 * t + n : n,
                        r++ % 4) ? o += String['fromCharCode'](255 & t >> (-2 * r & 6)) : 0)
                            n = i['indexOf'](n);
                        for (var d = 0, c = o['length']; d < c; d++)
                            a += '%' + ('00' + o['charCodeAt'](d)['toString'](16))['slice'](-2);
                        return decodeURIComponent(a);
                    }
                    ,
                    e = arguments,
                    a['khmYwP'] = !!1;
                }
                var r = t + n[0]
                  , s = e[r];
                return s ? o = s : (o = a['ZGUIrU'](o),
                e[r] = o),
                o;
            }
            ,
            a(e, t);
        }
        function r() {
            var e = ['DMLKzw8', 'Bw10', 'D2vIzhjPDMvYlwv2ywX1yxrL', 'zNrZB3zKCJi', 'yMr0', 'CxvLCNLtzwXLy3rVCKfSBa', 'zgrFBG', 'CMvUzgvYzxi', 'DMnODhm', 'tgLUDxG', 'jgnOCM9Tzv9HC3LUy1nJCMLWDeLUzM8', 'zw1PDa', 'yxvKAw8VBxaZoW', 'zgrFvW', 'CgX1', 'DhPW', 'rgf0zvrPBwvgB3jTyxq', 'D2vIzhjPDMvY', 'A2LUza', 'AxDNBa', 'D2vIr0XdAgvJAW', 'tgLIzxjHDgLVBIbtyw5Z', 'BwfUDwfSv2vIz2XdAgvJAW', 'zgrFuq', 'AgnVDMrYmG', 'ywnTCa', 'y29YCMvSyxrPB25FAwq', 'uM9IB3rV', 'x1DfqKrssvzfuL9ftevnx0nbq0Hf', 'zhjPDMvYlwv2ywX1yxrL', 'zgv2AwnLtwvTB3j5', 'BxbFC3K', 'BMrKyW', 'odDgmdm3odHfnZG1rKyZmdfeotbcqJe5n0u1odaZ', 'zgrFwG', 'CgX1z2LUCW', 'zxjY', 'zw51BwvYyxrLrgv2AwnLCW', 'D2LUzg93', 'z2X2za', 'rhjVAwqGu2fUCW', 'zgrFDgvZDgnVB2TPzt0XoYbWyxrOps87ifnHBwvtAxrLpuXHEdSGu2vJDxjL', 'C3r5Bgu', 'zgrFzq', 'AgnVDMrY', 'ywnTCdq', 'zgLZCgf0y2HfDMvUDa', 'zgrFyG', 'zgrFDG', 'DhrZDa', 'zgrFrq', 'zgrFsW', 'zgrFyw4', 'DMLKzw8VB2DNoYbJB2rLy3m9iNrOzw9Yysi', 'AgfYzhDHCMvdB25JDxjYzw5JEq', 'AgLKzgvU', 'DM5K', 'yNjFB2G', 'AxnuExbLu3vWCg9YDgvK', 'Bwf4', 'ywnV', 'y29UDgvUDfDPBMrVDW', 'C2XLDNq', 'BMf2AwDHDg9Y', 'tMf2AwDHDg9YvufeyxrH', 'uKvorevsrvi', 'zwnWyW', 'zgf0yq', 'jgnKy19HC2rQzMXHC3v0B3bMAhzJwKXTy2zSxW', 'ywnTyxrZ', 'ywnMDhm', 'x19Syxn0v2f0AxjbBgvYDa', 'AxbOB25L', 'zxHLy3v0zunOzwnRC09UtwfPBLrOCMvHza', 'AxnuCNvZDgvK', 'DxnLCKfNzw50rgf0yq', 'zMLSDgvY', 'z2v0tw91C2vqB3nPDgLVBG', 'zgjVDG', 'zgrFywO', 'CMvTB3zLrxzLBNrmAxn0zw5LCG', 'y29RExm', 'y2fJAgvF', 'ywnTCdm', 'y2HHCMDPBMC', 'C3rYx2LKyG', 'DwfgDwXSvMvYC2LVBG', 'ChjVzhvJDfn1yG', 'Bw91C2vKB3DU', 'AwrU', 'C3bHBG', 'sw50Ba', 'ChjVDg90ExbL', 'y2HLy2TqCMvJAxnLvgLTzxPVBMu', 'CgfYC2vjBNq', 'C2XHDa', 'DhLWzq', 'ig9IAMvJDcbJB3vSzcbUB3qGyMuGy2XVBMvKlG', 'zNrZB3zKCG', 'zgrFywy', 't3bLCMe', 'zgvMAw5Lza', 'zgrFvq', 'AgvPz2H0', 'DMnTCa', 'BgLUDxG', 'zxzHBfXZyxrCC2v2ywX1yxrLFebJAhjVBwv8zxzHBhvHDgva', 'D3DS', 'yxjZx3C', 'BwvZC2fNzq', 'AxnxB3jRzxjbDMfPBgfIBgu', 'y3zZ', 'z2v0', 'DMmXDhm', 'q29UDgfJDhnnyw5Hz2vY', 'zgrFDW', 'x19WCM90B19F', 'yMnKyq', 'DMmZ', 'yxjJAgL0zwn0DxjL', 'zgrFtq', 'C2v0vgLTzw91Da', 'zNvUy3rPB24', 'B2nWDa', 'BgDZB2q', 'y2HPBgrmAxn0', 'zgvSzxrLqwXSrerdB29RAwvZ', 'zgrFCW', 'DgLTzvn0yw1W', 'Bw1FBwq', 'DxnI', 'yw5KCM9Pza', 'Dgv4DenVBNrLBNq', 'C2v0uhjVDg90ExbLt2y', 'D2LKDgG', 'DMnO', 'BwfUDwfSy2HLy2TqCMvJAxnLvgLTzxPVBMu', 'CgvYBwLZC2LVBNm', 'C3fYDa', 'y2T3yq', 'zgLS', 'sfrntfzPzgvVrwXLBwvUDa', 'zgrFsG', 'ChjVy2vZCW', 'BMHP', 'BMfTzq', 'zxH0zxjUywW', 'zw10', 'B250B3vJAhn0yxj0', 'zgrFuW', 'BwfUDwfSq2HLy2TozwvKzwq', 'CgXNB2q', 'B3bLBKrHDgfIyxnL', 'D29YA2vYq2HLy2TuExbLCW', 'zwXLy3rYB24', 'AM9PBG', 'BwvKAwfezxzPy2vZ', 'y2HYB21L', 'CgXVDMrYmG', 'twLJCM9ZB2z0ifLHsgvP', 'zgrFqG', 'igC6', 'zxzHBfXZyxrCC2v4zwn1Dgvty3jPChq', 'CMvTB3zLq2HPBgq', 'zgrFBW', 'zgrFyxa', 'zgv2AwnLswq', 'yML0BMvZCW', 'zxDZAq', 'yxvKAw8VB2DNoYbJB2rLy3m9iNzVCMjPCYi', 'zgrFEq', 'DgjJzq', 'C2XPy2u', 'x193zwjKCML2zxjFC2nYAxb0x2zU', 'z2v0t3DUuhjVCgvYDhLezxnJCMLWDg9Y', 'y2zZzq', 'qw5KCM9Pza', 'yNjVD3nLCMzSB3CTy29UDgfPBMvY', 'CgXNBMu', 'zgrFwq', 'lYOQlW', 'D3D3lG', 'yxn5BMndAgfSBgvUz2vgAw5PC2HLza', 'y2XPzw50wq', 'zg9JDw1LBNq', 'DMLKzw8VCxvPy2T0Aw1LoW', 'zgrFzW', 'C3rYAw5N', 'CxvLCNLtzwXLy3rVCG', 'DMLKzw8VD2vIBtSGy29KzwnZpsj2CdGSihzVCMjPCYi', 'zgrFtG', 'DgfNChu', 'tM90BYbtyw5Z', 'Bw9IAwXL', 'zgrFywi', 'Dg9tDhjPBMC', 'C2nYzwvU', 'Bwf4vg91y2HqB2LUDhm', 'qNvMzMvY', 'vu5nqvnlrurFvKvore9sx1DfqKDm', 'zgrFza', 'twLTzvr5CgvbCNjHEq', 'Cg9ZAxrPB24', 'y3jLyxrLrxzLBNq', 'BgvUz3rO', 'BxnnyxHuB3vJAfbVAw50CW', 'DMLKzw8VBxa0oYbJB2rLy3m9iMf2mdeUmc4Woe0UmdGI', 'twf0Aa', 'zw1WDhK', 'C3rYx2XZ', 'Bw9KzwW', 'D29YA2vYq2HLy2TZvg9fEgvJDxrL', 'D3DSCNy', 'z2v0sw5MB0nSAwnR', 'y2zWCa', 'BNvHza', 'CgXHDgzVCM0', 'x19MEgrYAxzLCL91BNDYyxbWzwq', 'zgrFBq', 'Bg9JyxrPB24', 'C3f0', 'sw50zxjUzxqGrxHWBg9Yzxi', 'DgLTzvPVBMu', 'Dg9mB3DLCKnHC2u', 'zMLYzwzVEa', 'Dw5KzwzPBMvK', 'q2fSAwjYAq', 'yxvKAw8VywfJoW', 'yxbWzw5Kq2HPBgq', 'y29VA2LL', 'D2r3', 'BxbFC3G', 'BwfJ', 'q2HYB21L', 'Au9t', 'DMvYC2LVBNm', 'yMLK', 'yM9KEq', 'D2rPzNjT', 'zgf0yurVBwvxB3jRzxjfDMvUDe5HBwu', 'DMnVDhm', 'x19KCML2zxjFzxzHBhvHDgu', 'Bw1TBw1TBw1TD3D3D3D3DW', 'yNrVyq', 'y2XPy2S', 'BMnSywq', 'z2v0ugfYyw1LDgvY', 'zgrFAG', 'C3bSAxq', 'zgrFywK', 'y2HLy2TnB3vZzvbVC2L0Aw9U', 'y2fSBfbOyw50B20', 'C3bHD24', 'x19Syxn0v2f0AxjdB25MAxjT', 'D2rPzG', 'y2XPzw50wa', 'ChvZAa', 'zgrFEG', 'yxvKAw8VBxa0oW', 'y2fUDMfZ', 'yxn5BMnOCM9UAxPLvgfZAW', 'zhaW', 'zgrFEa', 'DgvYBwLUyxrL', 'ywrKrxzLBNrmAxn0zw5LCG', 'yxvKAw8VD2f2oYbJB2rLy3m9iJeI', 'v2LUzg93CYbqAg9Uzq', 'y2XPzw50sgvPz2H0', 'AgfZt3DUuhjVCgvYDhK', 'Bw92zw1LBNrz', 'AgrU', 'BgfIzwW', 'yMnS', 'DxnLCKfNzw50', 'zgrQC2TLEq', 'DgfYz2v0', 'BgfUz3vHz2u', 'zxzHBhvHDgu', 'zgrFCa', 'y2fUugXHEvr5Cgu', 'z2v0rwXLBwvUDej5swq', 'zgrFywS', 'ugvYBwLZC2LVBLn0yxr1CW', 'zg9Tqxv0B21HDgLVBG', 'B25TzxnZywDL', 'ywnTCdr0CW', 'ANnM', 'x2LMCMfTzvjLzG', 'DMmZDhm', 'ufqGu2fUCW', 'ywnTChrZ', 'zw1K', 'y2f0y2G', 'z2XYza', 'BM9Uzq', 'x2rKDhD2', 'DgHLBG', 'DhnFBxrW', 'D3nKyW', 'zgf0yurVBwvuB29SCW', 'CgfYzw50rwXLBwvUDa', 'v0vcr0XFzgvIDwDFCMvUzgvYzxjFAw5MBW', 'C2vSzG', 'C2vYAwfSAxPLvg9tDhjPBMC', 'rxjYoIa', 'yxvKAw8VEc1Tnge7', 'rxjYB3i', 'zNbO', 'zgrFrG', 'zgrFywm', 'zwTYCa', 'Aw5KzxHpzG', 'z2v0qMf0DgvYEq', 'zgvSDgfwywXZ', 'BxbFy3K', 'z3jVDxbjza', 'C2nYzwvUwq', 'v29YA2vYq2f1z2H0rxjYoIa', 'ywmZ', 'CgXNz3q', 'uhjVDg90ExbL', 'y2rJx2fKB1fWB2fZBMzHnZzWzMnAtg1JzMXFqxjYyxK', 'Bwf0y2G', 'z2v0vgLTzxPVBMvpzMzZzxq', 'zxzH', 'y3jLyxrLrwXLBwvUDa', 'zw51BwvYywjSzq'];
            return (r = function() {
                return e;
            }
            )();
        }
'''


if __name__ == '__main__':
    with open('tags.js', 'r') as f:
        content = f.read()
        matches = finditer(r"'(?P<name>(\\x[0-9A-Fa-f]{2})+)'", content, MULTILINE)
        actualNames = {}
        for match in matches:
            actualNames[match.group('name')] = match.group('name').encode().decode('unicode_escape').replace("'", "\\'")
       
        sortNames = sorted(actualNames.keys(), key=len, reverse=True)
        for name in sortNames:
            content = content.replace(name, actualNames[name])

        if os.path.exists('mapping.txt'):
            os.remove('mapping.txt')
        
        with open('mapping.txt', 'a+') as w:
            for k,v in actualNames.items():
                w.write(f'{v}={k}\n')

        methods = {}
        matches = finditer(r"\W(?P<method>\w\((?P<number>\d+)\))", content, MULTILINE)
        numberMapper = {}
        for match in matches:
            methods[match.group('method')] = match.group('number')
            numberMapper[match.group('number')] = None

        findVarEncryptName = compile(execJs)
        totalSpent = 0
        for key in numberMapper.keys():
            n = datetime.now()
            numberMapper[key] = findVarEncryptName.call('a', key)
            spent = int((datetime.now() - n).total_seconds() * 1000)
            totalSpent += spent
            print(f'resolve:{key}, result:{numberMapper[key]}, use:({spent}ms)')
        print(f'Done use {totalSpent}MS')

        for k, v in methods.items():
            methods[k] = f"'{numberMapper[v]}'"

        if os.path.exists('method.txt'):
            os.remove('method.txt')

        with open('method.txt', 'a+') as w:
            for k,v in methods.items():
                w.write(f'{k}={v}\n')
                content = content.replace(k, v)

        with open('datadome.js', 'w') as w:
            w.write(content)
        