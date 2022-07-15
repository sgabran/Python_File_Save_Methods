# ver = '2022-7-15-1'

import os
import os.path
import pandas as pd
import numpy as np


class FileSaveMethods:

    # SAMPLE FOR SAVE_FILES() TO BE USED IN MAIN CODE
    # def save_files(self):
    #     # Check if data exists
    #     data_ready = False
    #     if self.session_preprocess is None:
    #         pass
    #     elif self.session_preprocess is not None:
    #         try:
    #             if hasattr(self.session_preprocess, 'smoothed_blw_removed_smoothed'):
    #                 data_ready = True
    #
    #         except NameError:
    #             pass
    #
    #     if data_ready is False:
    #         messagebox.showerror(title="Save Files", message="No Data Loaded")
    #
    #     else:
    #         # Save data_to_process_np
    #         file_name = str(self.user_entry.file_name + '_raw')
    #         filesave.FileSaveMethods.start_save_csv(file_name, self.session_preprocess.data_to_process_np,
    #                                             self.user_entry.file_location)
    #
    #         # Save smoothed_blw_removed_smoothed data
    #         file_name = str(self.user_entry.file_name + '_processed')
    #         filesave.FileSaveMethods.start_save_csv(file_name, self.session_preprocess.smoothed_blw_removed_smoothed,
    #                                                 self.user_entry.file_location)

    @staticmethod
    def start_save_csv(file_name, data, file_location):
        message, colour = FileSaveMethods.save_csv_single_column(file_name, data, file_location)
        return message, colour

    @staticmethod
    def save_csv_single_column(file_name, data, file_location):
        message, colour = FileSaveMethods.save_data_pandas_single_column(file_name, data, file_location)
        return message, colour

    @staticmethod
    def save_data_pandas_single_column(file_name, data, file_location):
        file_full_address = (file_location + "/" + file_name + '.csv')
        if os.path.isfile(file_full_address):
            message = "File Exists and Will Be Overwritten: " + str(file_full_address) + "\n"
            colour = 'red'
        else:
            message = "File Saved: " + str(file_full_address) + "\n"
            colour = 'blue'

        pd.DataFrame(data).to_csv(file_full_address, header=False, index=False)

        return message, colour

    # @staticmethod
    # def save_csv(file_name, file_name_save, data, file_location, delimiter):
    #     file_name = str(file_name + file_name_save)
    #
    #     # if timestamp_include:
    #     #     data_to_write = self.session_process_csv.data_requested_timestamp_np
    #     # else:
    #     #     data_to_write = self.session_process_csv.data_requested_np
    #
    #     # if self.user_entry.header_include_files:
    #     #     np.insert(data_to_write, 0, str(self.session_process_csv.header_list_np))#, axis=None)
    #
    #     # if self.user_entry.header_include_plots:
    #     #     pass
    #     # else:
    #     FileSaveMethods.save_data_pandas_single_column(file_location, file_name, data, delimiter)

    # @staticmethod
    # def save_data_pandas_delimiter(file_location, file_name, data_to_write, delimiter):
    #     file_full_address = (file_location + "/" + file_name + '.csv')
    #     if os.path.isfile(file_full_address):
    #         self.session_log.write_textbox("File Exists and Will Be Overwritten: ", "red")
    #     if delimiter == DELIMITER_TYPE_COMMA:
    #         pd.DataFrame(data_to_write).to_csv(file_full_address, header=False, index=False, sep=',')
    #     elif delimiter == DELIMITER_TYPE_TAB:
    #         pd.DataFrame(data_to_write).to_csv(file_full_address, header=False, index=False, sep='\t')
    #
    # # def _save_data_pandas_header_delimiter(self, folder, file_name, data, header_list, delimiter):
    # #     file_full_address = (folder + "/" + file_name + '.csv')
    # #     if os.path.isfile(file_full_address):
    # #         self.session_log.write_textbox("File Exists and Will Be Overwritten: ", "red")
    #
    #     if delimiter == DELIMITER_TYPE_COMMA:
    #         pd.DataFrame(data).to_csv(file_full_address, index=False, header=header_list, sep=',')
    #     elif delimiter == DELIMITER_TYPE_TAB:
    #         pd.DataFrame(data).to_csv(file_full_address, index=False, header=header_list, sep='\t')
