// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Acm
{
    /// <summary>
    /// This resource represents a successful validation of an ACM certificate in concert
    /// with other resources.
    /// 
    /// Most commonly, this resource is used together with `aws.route53.Record` and
    /// `aws.acm.Certificate` to request a DNS validated certificate,
    /// deploy the required validation records and wait for validation to complete.
    /// 
    /// &gt; **WARNING:** This resource implements a part of the validation workflow. It does not represent a real-world entity in AWS, therefore changing or deleting this resource on its own has no immediate effect.
    /// 
    /// 
    /// 
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/acm_certificate_validation.html.markdown.
    /// </summary>
    public partial class CertificateValidation : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the certificate that is being validated.
        /// </summary>
        [Output("certificateArn")]
        public Output<string> CertificateArn { get; private set; } = null!;

        /// <summary>
        /// List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation
        /// </summary>
        [Output("validationRecordFqdns")]
        public Output<ImmutableArray<string>> ValidationRecordFqdns { get; private set; } = null!;


        /// <summary>
        /// Create a CertificateValidation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CertificateValidation(string name, CertificateValidationArgs args, CustomResourceOptions? options = null)
            : base("aws:acm/certificateValidation:CertificateValidation", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private CertificateValidation(string name, Input<string> id, CertificateValidationState? state = null, CustomResourceOptions? options = null)
            : base("aws:acm/certificateValidation:CertificateValidation", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing CertificateValidation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CertificateValidation Get(string name, Input<string> id, CertificateValidationState? state = null, CustomResourceOptions? options = null)
        {
            return new CertificateValidation(name, id, state, options);
        }
    }

    public sealed class CertificateValidationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the certificate that is being validated.
        /// </summary>
        [Input("certificateArn", required: true)]
        public Input<string> CertificateArn { get; set; } = null!;

        [Input("validationRecordFqdns")]
        private InputList<string>? _validationRecordFqdns;

        /// <summary>
        /// List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation
        /// </summary>
        public InputList<string> ValidationRecordFqdns
        {
            get => _validationRecordFqdns ?? (_validationRecordFqdns = new InputList<string>());
            set => _validationRecordFqdns = value;
        }

        public CertificateValidationArgs()
        {
        }
    }

    public sealed class CertificateValidationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the certificate that is being validated.
        /// </summary>
        [Input("certificateArn")]
        public Input<string>? CertificateArn { get; set; }

        [Input("validationRecordFqdns")]
        private InputList<string>? _validationRecordFqdns;

        /// <summary>
        /// List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation
        /// </summary>
        public InputList<string> ValidationRecordFqdns
        {
            get => _validationRecordFqdns ?? (_validationRecordFqdns = new InputList<string>());
            set => _validationRecordFqdns = value;
        }

        public CertificateValidationState()
        {
        }
    }
}
