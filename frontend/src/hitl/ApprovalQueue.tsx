import React, { useState } from "react";
import ApprovalModal from "./ApprovalModal";

export interface ApprovalRequest {
  id: string;
  company_name: string;
  contact_name: string;
  recommendation: string;
  status: string;
}

interface Props {
  approvals: ApprovalRequest[];

  onApprove: (
    approvalId: string
  ) => Promise<void>;

  onReject: (
    approvalId: string
  ) => Promise<void>;
}

const ApprovalQueue: React.FC<Props> = ({
  approvals,
  onApprove,
  onReject
}) => {
  const [selected, setSelected] =
    useState<ApprovalRequest | null>(
      null
    );

  const [open, setOpen] =
    useState(false);

  const openModal = (
    approval: ApprovalRequest
  ) => {
    setSelected(approval);
    setOpen(true);
  };

  const closeModal = () => {
    setSelected(null);
    setOpen(false);
  };

  return (
    <>
      <div className="bg-white rounded-lg shadow p-5">
        <h2 className="text-xl font-bold mb-4">
          Approval Queue
        </h2>

        <div className="space-y-3">
          {approvals.map((approval) => (
            <div
              key={approval.id}
              className="border rounded-lg p-4 flex justify-between items-center"
            >
              <div>
                <div className="font-semibold">
                  {approval.company_name}
                </div>

                <div className="text-sm text-gray-500">
                  {approval.contact_name}
                </div>
              </div>

              <button
                onClick={() =>
                  openModal(approval)
                }
                className="bg-blue-600 text-white px-4 py-2 rounded"
              >
                Review
              </button>
            </div>
          ))}
        </div>
      </div>

      <ApprovalModal
        item={selected}
        isOpen={open}
        onClose={closeModal}
        onApprove={async (id) => {
          await onApprove(id);
          closeModal();
        }}
        onReject={async (id) => {
          await onReject(id);
          closeModal();
        }}
      />
    </>
  );
};

export default ApprovalQueue;