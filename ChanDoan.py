from experta import *
import ast


class ChuyenGiaYTe(KnowledgeEngine):
    nguoi_dung = "",

    @DefFacts()
    def du_lieu_can_thiet(self):
        """
        Đây là một phương thức được gọi mỗi khi ChanDoan.reset() được gọi..
        Nó hoạt động giống như một phương thức khởi tạo cho lớp này.
        """
        yield Fact(F_timBenh = 'true')
        print("Chào! Doctor Đức đây!\n\nỞ đây có chẩn đoán bệnh miễn phí!\nVui lòng trả lời các câu hỏi sau :)))\n\n")


    @Rule(Fact(F_timBenh = 'true'),NOT(Fact(F_ten=W())),salience = 1000)
    def hoi_ten(self):
        self.nguoi_dung = input("Nhập tên của bạn vào đi? chờ gì nữa?\n")
        self.declare(Fact(F_ten=self.nguoi_dung))

    @Rule(Fact(F_timBenh='true'), NOT (Fact(F_tucNguc = W())),salience = 995)
    def bi_tuc_nguc(self):
        self.tuc_nguc = input("\nBạn có bị đau ngực hông?\nVui lòng nhập Yes/No\n")
        self.tuc_nguc = self.tuc_nguc.lower()
        self.declare(Fact(F_tucNguc = self.tuc_nguc.strip().lower()))

    # @Rule(Fact(F_timBenh='true'), (Fact(F_tucNguc = 'yes')),salience = 990)
    # def biTucNgucDuDoi(self):
    #     self.tuc_nguc_du_doi = input("\nNó có quá nghiêm trọng hông?\nVui lòng nhập Yes / No\n")
    #     self.declare(Fact(F_tucNgucDuDoi = self.tuc_nguc_du_doi.strip().lower()))

    @Rule(Fact(F_timBenh='true'), NOT (Fact(F_ho = W())),salience = 985)
    def bi_ho(self):
        self.ho = input("\nBạn có bị ho hông?\nVui lòng nhập Yes/No\n")
        self.ho = self.ho.lower()
        self.declare(Fact(F_ho = self.ho.strip().lower()))


    # @Rule(Fact(F_timBenh='true'), (Fact(F_ho = 'yes')),salience = 980)
    # def bi_ho_du_doi(self):
    #     self.ho_du_doi = input("\nBạn có bị ho nặng hông?\nVui lòng nhập Yes / No\n")
    #     self.declare(Fact(F_tucNgucDuDoi = self.ho_du_doi.strip().lower()))


    @Rule(Fact(F_timBenh='true'), NOT (Fact(F_ngatXiu = W())),salience = 975)
    def bi_ngat_xiu(self):
        self.ngat_xiu = input("\nThỉnh thoảng bạn có ngất xỉu hông?\nVui lòng nhập Yes/No\n")
        self.ngat_xiu = self.ngat_xiu.lower()
        self.declare(Fact(F_ngatXiu = self.ngat_xiu.strip().lower()))


    @Rule(Fact(F_timBenh='true'), NOT (Fact(F_metMoi = W())),salience = 970)
    def bo_met_moi(self):
        self.met_moi = input("\nĐôi khi bạn có cảm thấy mệt mỏi?\nVui lòng nhập Yes/No\n")
        self.met_moi = self.met_moi.lower()
        self.declare(Fact(F_metMoi = self.met_moi.strip().lower()))

    @Rule(Fact(F_timBenh='true'), NOT (Fact(F_nhucDau = W())),salience = 965)
    def bi_nhuc_dau(self):
        self.nhuc_dau = input("\nBạn có thấy đau đầu hông?\nVui lòng nhập Yes/No\n")
        self.nhuc_dau = self.nhuc_dau.lower()
        self.declare(Fact(F_nhucDau = self.nhuc_dau.strip().lower()))

    # @Rule(Fact(F_timBenh='true'), (Fact(F_nhucDau = 'yes')),salience = 960)
    # def bi_nhuc_dau_du_doi(self):
    #     self.nhuc_dau_du_doi = input("\nNó có quá nghiêm trọng hông?\nPVui lòng nhập Yes / No\n")
    #     self.declare(Fact(F_nhucDauDuDoi = self.nhuc_dau_du_doi.strip().lower()))

    @Rule(Fact(F_timBenh='true'), NOT (Fact(F_dauLung = W())),salience = 955)
    def bi_dau_lung(self):
        self.dau_lung = input("\nBạn có bị đau lưng hông?\nVui lòng nhập Yes/No\n")
        self.dau_lung = self.dau_lung.lower()
        self.declare(Fact(F_dauLung = self.dau_lung.strip().lower()))

    @Rule(Fact(F_timBenh='true'), NOT (Fact(F_trungMat = W())),salience = 950)
    def bi_trung_mat(self):
        self.trung_mat = input("\nBạn có bị trũng mắt hông?\nVui lòng nhập Yes/No\n")
        self.trung_mat = self.trung_mat.lower()
        self.declare(Fact(F_trungMat = self.trung_mat.strip().lower()))

    @Rule(Fact(F_timBenh='true'), NOT (Fact(F_sot = W())),salience = 945)
    def bi_sot(self):
        self.sot = input("\nBạn có bị sốt hông?\nVui lòng nhập Yes/No\n")
        self.sot=self.sot.lower()
        self.declare(Fact(F_sot = self.sot.strip().lower()))

    @Rule(Fact(F_timBenh='true'), NOT (Fact(F_dauHong = W())),salience = 940)
    def bi_dau_hong(self):
        self.dau_hong = input("\nBạn có bị đau họng hông?\nVui lòng nhập Yes/No\n")
        self.dau_hong = self.dau_hong.lower()
        self.declare(Fact(F_dauHong = self.dau_hong.strip().lower()))

    @Rule(Fact(F_timBenh='true'), NOT (Fact(F_bonChon = W())),salience = 935)
    def bi_bon_chon(self):
        self.bon_chon = input("\nBạn có cảm thấy bồn chồn hông?\nVui lòng nhập Yes/No\n")
        self.bon_chon = self.bon_chon.lower()
        self.declare(Fact(F_bonChon = self.bon_chon.strip().lower()))

#=================================================================================

    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'no'), Fact(F_ho = 'yes'), Fact(F_ngatXiu = 'no'),Fact(F_metMoi = 'no'),
    Fact(F_nhucDau = 'no'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'no'),Fact(F_sot = 'yes'),Fact(F_dauHong='no'),
    Fact(F_bonChon = 'no'))
    def benh_0(self):
        self.declare(Fact(F_benh = 'Covid'))

    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'yes'), Fact(F_ho = 'no'), Fact(F_ngatXiu = 'no'),Fact(F_metMoi = 'yes'),
    Fact(F_nhucDau = 'no'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'no'),Fact(F_sot = 'no'),Fact(F_dauHong='no'),
    Fact(F_bonChon = 'no'))
    def benh_1(self):
        self.declare(Fact(F_benh = 'Alzheimers'))

    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'no'), Fact(F_ho = 'no'), Fact(F_ngatXiu = 'no'),Fact(F_metMoi = 'yes'),
    Fact(F_nhucDau = 'no'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'yes'),Fact(F_sot = 'no'),Fact(F_dauHong='no'),
    Fact(F_bonChon = 'no'))
    def benh_2(self):
        self.declare(Fact(F_benh = 'Hen_suyen'))

    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'no'), Fact(F_ho = 'no'), Fact(F_ngatXiu = 'no'),Fact(F_metMoi = 'yes'),
    Fact(F_nhucDau = 'no'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'no'),Fact(F_sot = 'no'),Fact(F_dauHong='no'),
    Fact(F_bonChon = 'yes'))
    def benh_3(self):
        self.declare(Fact(F_benh = 'Tieu_duong'))


    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'no'), Fact(F_ho = 'no'), Fact(F_ngatXiu = 'no'),Fact(F_metMoi = 'no'),
    Fact(F_nhucDau = 'yes'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'yes'),Fact(F_sot = 'no'),Fact(F_dauHong='no'),
    Fact(F_bonChon = 'no'))
    def benh_4(self):
        self.declare(Fact(F_benh = 'Dong_kinh'))


    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'no'), Fact(F_ho = 'no'), Fact(F_ngatXiu = 'no'),Fact(F_metMoi = 'no'),
    Fact(F_nhucDau = 'no'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'yes'),Fact(F_sot = 'yes'),Fact(F_dauHong='yes'),
    Fact(F_bonChon = 'no'))
    def benh_5(self):
        self.declare(Fact(F_benh = 'Tang_nhan_ap'))

    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'no'), Fact(F_ho = 'no'), Fact(F_ngatXiu = 'yes'),Fact(F_metMoi = 'no'),
    Fact(F_nhucDau = 'no'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'no'),Fact(F_sot = 'no'),Fact(F_dauHong='no'),
    Fact(F_bonChon = 'no'))
    def benh_6(self):
        self.declare(Fact(F_benh = 'Benh_tim'))

    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'no'), Fact(F_ho = 'no'), Fact(F_ngatXiu = 'yes'),Fact(F_metMoi = 'no'),
    Fact(F_nhucDau = 'no'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'no'),Fact(F_sot = 'yes'),Fact(F_dauHong='no'),
    Fact(F_bonChon = 'no'))
    def benh_7(self):
        self.declare(Fact(F_benh = 'Say_nang'))

    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'no'), Fact(F_ho = 'no'), Fact(F_ngatXiu = 'no'),Fact(F_metMoi = 'no'),
    Fact(F_nhucDau = 'no'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'yes'),Fact(F_sot = 'no'),Fact(F_dauHong='no'),
    Fact(F_bonChon = 'yes'))
    def benh_8(self):
        self.declare(Fact(F_benh = 'Cuong_giap'))

    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'yes'), Fact(F_ho = 'no'), Fact(F_ngatXiu = 'no'),Fact(F_metMoi = 'yes'),
    Fact(F_nhucDau = 'no'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'no'),Fact(F_sot = 'no'),Fact(F_dauHong='yes'),
    Fact(F_bonChon = 'no'))
    def benh_9(self):
        self.declare(Fact(F_benh = 'Ha_than_nhiet'))

    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'no'), Fact(F_ho = 'yes'), Fact(F_ngatXiu = 'no'),Fact(F_metMoi = 'no'),
    Fact(F_nhucDau = 'yes'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'no'),Fact(F_sot = 'yes'),Fact(F_dauHong='no'),
    Fact(F_bonChon = 'no'))
    def benh_10(self):
        self.declare(Fact(F_benh = 'Vang_da'))

    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'no'), Fact(F_ho = 'no'), Fact(F_ngatXiu = 'no'),Fact(F_metMoi = 'no'),
    Fact(F_nhucDau = 'yes'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'no'),Fact(F_sot = 'yes'),Fact(F_dauHong='yes'),
    Fact(F_bonChon = 'no'))
    def benh_11(self):
        self.declare(Fact(F_benh = 'Viem_xoang'))

    @Rule(Fact(F_timBenh='true'),Fact(F_tucNguc = 'no'), Fact(F_ho = 'no'), Fact(F_ngatXiu = 'no'),Fact(F_metMoi = 'yes'),
    Fact(F_nhucDau = 'no'),Fact(F_dauLung = 'no'),Fact(F_trungMat = 'yes'),Fact(F_sot = 'yes'),Fact(F_dauHong='no'),
    Fact(F_bonChon = 'yes'))
    def benh_12(self):
        self.declare(Fact(F_benh = 'Benh_lao'))


    @Rule(Fact(F_timBenh='true'),NOT (Fact(F_benh = W())),salience = -1)
    def khong_khop(self):
        self.declare(Fact(F_benh = 'KhongXacDinh'))

    @Rule(Fact(F_timBenh = 'true'),Fact(F_benh = MATCH.benh),salience = 1)
    def mac_benh(self, benh):

        if(benh == 'KhongXacDinh'):
            trieuChung = []
            trieuChung.append('dau_lung')
            trieuChung.append('tuc_nguc')
            trieuChung.append('ho')
            trieuChung.append('ngat_xiu')
            trieuChung.append('met_moi')
            trieuChung.append('sot')
            trieuChung.append('nhuc_dau')
            trieuChung.append('dau_hong')
            trieuChung.append('bon_chon')
            trieuChung.append('trung_mat')
            print('\n\nTôi đã kiểm tra các triệu chứng sau:',trieuChung)
            trieuChung_DS=[self.dau_lung,self.tuc_nguc,self.ho,self.ngat_xiu,self.met_moi,self.sot,self.nhuc_dau,self.dau_hong,self.bon_chon,self.trung_mat]
            print('\n\nCác triệu chứng ở bệnh nhân:',trieuChung_DS)

            file = open("TrieuChungCuaBenh.txt", "r", encoding="utf-8")
            noiDung = file.read()
            tuDien = ast.literal_eval(noiDung)
            file.close()

            co_trieuChung = []
            for i in range(0,len(trieuChung_DS)):
                if trieuChung_DS[i] == 'yes':
                    co_trieuChung.append(trieuChung[i])

            gtri_toi_da = 0
            print('\n\nCó các triệu chứng nhận thấy là : ', co_trieuChung,"\n")
            for tuKhoa in tuDien.keys():
                gtri = tuDien[tuKhoa].split(",")
                dem = 0
                print(tuKhoa,":",gtri)
                for x in gtri:
                    if x in co_trieuChung:
                        dem+=1
                # print('Triệu Chứng:',dem)
                if dem > gtri_toi_da:
                    gtri_toi_da = dem
                    chan_doan = tuKhoa

            if gtri_toi_da == 0:
                print("\nKhông bị làm sao thì đi khám cho vui à? Về nhà đi bạn :)))")
            else:
                print("\n\nTôi không thể tự tin cho bạn biết chính xác căn bệnh nhưng tôi đoán là bạn đang mắc phải",chan_doan)

                print('\n---------------------------------------------------------------------------')

                print ('\n\nMột số thông tin về bệnh:',chan_doan)

                f = open("benh/mo_ta_benh/" + chan_doan + ".txt", "r", encoding="utf-8")
                print(f.read())
                print('---------------------------------------------------------------------------')
                print('\n\n',self.nguoi_dung,',không cần phải lo lắng','. Chúng tôi thậm chí có một số biện pháp phòng ngừa cho bạn!\n')
                f = open("benh/phuong_phap_dieu_tri/" + chan_doan + ".txt", "r", encoding="utf-8")
                print(f.read())
                print('\n---------------------------------------------------------------------------')
        else:
            print('Có thể bạn đang mắc phải:',benh)
            print('\n\n')
            print('\n---------------------------------------------------------------------------')
            print('Một số thông tin về bệnh:\n')
            print(benh)
            f = open("benh/mo_ta_benh/" + benh + ".txt", "r", encoding="utf-8")
            print(f.read())
            print('\n---------------------------------------------------------------------------')
            print('\n\n', self.nguoi_dung,',không cần phải lo lắng','. Chúng tôi thậm chí có một số biện pháp phòng ngừa cho bạn!\n')
            f = open("benh/phuong_phap_dieu_tri/" + benh + ".txt", "r", encoding="utf-8")
            print(f.read())
    # @Rule(Fact(F_timBenh = 'true'),
    # Fact(F_ten=MATCH.ten))
    # def chao_hoi(self, ten):
    #     print("Xin chào!",ten, "Thời tiết hôm nay thế nào?")
if __name__ == "__main__":
    ChanDoan = ChuyenGiaYTe()
    ChanDoan.reset()
    ChanDoan.run()
    print('\nIn dữ kiện động cơ sau 1 lần chạy',ChanDoan.facts)
