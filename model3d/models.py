from django.db import models

class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d')

class UploadManager(models.Model):
    filepath = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    uploaded_by_user = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField('date uploaded')

    # TODO
    # Processing audit information later on
    PENDING, PROCESSED, FAILED = 'Pending', 'Processed', 'Failed'

    STATUSES = (
        (PENDING, 'Pending'),
        (PROCESSED, 'Processed'),
        (FAILED, 'Failed'),
    )

    # status = models.CharField(max_length=64, choices=STATUSES, default=PENDING)
    # processing_description = models.TextField(blank=True, null=True)
    # num_records = models.PositiveIntegerField()
    # date_start_processing = models.DateTimeField(null=True)
    # date_end_processing = models.DateTimeField(null=True)
    #
    # def process(self):
    #     self.date_start_processing = datetime.datetime.now()
    #     try:
    #         # process upload data,
    #         print "processing upload data"
    #     except Exception, e:
    #         self._mark_failed(unicode(e))
    #     else:
    #         self._mark_processed(num_records)
    #
    # def _mark_processed(self, num_records, description=None):
    #     self.status = self.PROCESSED
    #     self.date_end_processing = datetime.datetime.now()
    #     self.num_records = num_records
    #     self.processing_description = description
    #     self.save()
    #
    # def _mark_failed(self, description):
    #     self.status = self.FAILED
    #     self.processing_description = description
    #     self.save()
    #
    # @property
    # def filename(self):
    #     return os.path.basename(self.filename)
    #
    # def was_processing_successful(self):
    #     return self.status == self.PROCESSED